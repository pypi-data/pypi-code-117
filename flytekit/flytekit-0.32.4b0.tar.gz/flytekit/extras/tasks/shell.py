import datetime
import os
import string
import subprocess
import typing
from dataclasses import dataclass

import flytekit
from flytekit.core.context_manager import ExecutionParameters
from flytekit.core.interface import Interface
from flytekit.core.python_function_task import PythonInstanceTask
from flytekit.core.task import TaskPlugins
from flytekit.loggers import logger
from flytekit.types.directory import FlyteDirectory
from flytekit.types.file import FlyteFile


@dataclass
class OutputLocation:
    """
    Args:
        var: str The name of the output variable
        var_type: typing.Type The type of output variable
        location: os.PathLike The location where this output variable will be written to or a regex that accepts input
                  vars and generates the path. Of the form ``"{{ .inputs.v }}.tmp.md"``.
                  This example for a given input v, at path `/tmp/abc.csv` will resolve to `/tmp/abc.csv.tmp.md`
    """

    var: str
    var_type: typing.Type
    location: typing.Union[os.PathLike, str]


def _dummy_task_func():
    """
    A Fake function to satisfy the inner PythonTask requirements
    """
    return None


class AttrDict(dict):
    """
    Convert a dictionary to an attribute style lookup. Do not use this in regular places, this is used for
    namespacing inputs and outputs
    """

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class _PythonFStringInterpolizer:
    """A class for interpolating scripts that use python string.format syntax"""

    class _Formatter(string.Formatter):
        def format_field(self, value, format_spec):
            """
            Special cased return for the given value. Given the type returns the string version for
            the type. Handles FlyteFile and FlyteDirectory specially.
            Downloads and returns the downloaded filepath.
            """
            if isinstance(value, FlyteFile):
                value.download()
                return value.path
            if isinstance(value, FlyteDirectory):
                value.download()
                return value.path
            if isinstance(value, datetime.datetime):
                return value.isoformat()
            return super().format_field(value, format_spec)

    def interpolate(
        self,
        tmpl: str,
        inputs: typing.Optional[typing.Dict[str, str]] = None,
        outputs: typing.Optional[typing.Dict[str, str]] = None,
    ) -> str:
        """
        Interpolate python formatted string templates with variables from the input and output
        argument dicts. The result is non destructive towards the given template string.
        """
        inputs = inputs or {}
        outputs = outputs or {}
        inputs = AttrDict(inputs)
        outputs = AttrDict(outputs)
        consolidated_args = {
            "inputs": inputs,
            "outputs": outputs,
            "ctx": flytekit.current_context(),
        }
        try:
            return self._Formatter().format(tmpl, **consolidated_args)
        except KeyError as e:
            raise ValueError(f"Variable {e} in Query not found in inputs {consolidated_args.keys()}")


T = typing.TypeVar("T")


class ShellTask(PythonInstanceTask[T]):
    """ """

    def __init__(
        self,
        name: str,
        debug: bool = False,
        script: typing.Optional[str] = None,
        script_file: typing.Optional[str] = None,
        task_config: T = None,
        inputs: typing.Optional[typing.Dict[str, typing.Type]] = None,
        output_locs: typing.Optional[typing.List[OutputLocation]] = None,
        **kwargs,
    ):
        """
        Args:
            name: str Name of the Task. Should be unique in the project
            debug: bool Print the generated script and other debugging information
            script: The actual script specified as a string
            script_file: A path to the file that contains the script (Only script or script_file) can be provided
            task_config: T Configuration for the task, can be either a Pod (or coming soon, BatchJob) config
            inputs: A Dictionary of input names to types
            output_locs: A list of :py:class:`OutputLocations`
            **kwargs: Other arguments that can be passed to :ref:class:`PythonInstanceTask`
        """
        if script and script_file:
            raise ValueError("Only either of script or script_file can be provided")
        if not script and not script_file:
            raise ValueError("Either a script or script_file is needed")
        if script_file:
            if not os.path.exists(script_file):
                raise ValueError(f"FileNotFound: the specified Script file at path {script_file} cannot be loaded")
            script_file = os.path.abspath(script_file)

        if task_config is not None:
            if str(type(task_config)) != "flytekitplugins.pod.task.Pod":
                raise ValueError("TaskConfig can either be empty - indicating simple container task or a PodConfig.")

        # Each instance of NotebookTask instantiates an underlying task with a dummy function that will only be used
        # to run pre- and post- execute functions using the corresponding task plugin.
        # We rename the function name here to ensure the generated task has a unique name and avoid duplicate task name
        # errors.
        # This seem like a hack. We should use a plugin_class that doesn't require a fake-function to make work.
        plugin_class = TaskPlugins.find_pythontask_plugin(type(task_config))
        self._config_task_instance = plugin_class(task_config=task_config, task_function=_dummy_task_func)
        # Rename the internal task so that there are no conflicts at serialization time. Technically these internal
        # tasks should not be serialized at all, but we don't currently have a mechanism for skipping Flyte entities
        # at serialization time.
        self._config_task_instance._name = f"_bash.{name}"
        self._script = script
        self._script_file = script_file
        self._debug = debug
        self._output_locs = output_locs if output_locs else []
        self._interpolizer = _PythonFStringInterpolizer()
        outputs = self._validate_output_locs()
        super().__init__(
            name,
            task_config,
            task_type=self._config_task_instance.task_type,
            interface=Interface(inputs=inputs, outputs=outputs),
            **kwargs,
        )

    def _validate_output_locs(self) -> typing.Dict[str, typing.Type]:
        outputs = {}
        for v in self._output_locs:
            if v is None:
                raise ValueError("OutputLocation cannot be none")
            if not isinstance(v, OutputLocation):
                raise ValueError("Every output type should be an output location on the file-system")
            if v.location is None:
                raise ValueError(f"Output Location not provided for output var {v.var}")
            if not issubclass(v.var_type, FlyteFile) and not issubclass(v.var_type, FlyteDirectory):
                raise ValueError(
                    "Currently only outputs of type FlyteFile/FlyteDirectory and their derived types are supported"
                )
            outputs[v.var] = v.var_type
        return outputs

    @property
    def script(self) -> typing.Optional[str]:
        return self._script

    @property
    def script_file(self) -> typing.Optional[os.PathLike]:
        return self._script_file

    def pre_execute(self, user_params: ExecutionParameters) -> ExecutionParameters:
        return self._config_task_instance.pre_execute(user_params)

    def execute(self, **kwargs) -> typing.Any:
        """
        Executes the given script by substituting the inputs and outputs and extracts the outputs from the filesystem
        """
        logger.info(f"Running shell script as type {self.task_type}")
        if self.script_file:
            with open(self.script_file) as f:
                self._script = f.read()

        outputs: typing.Dict[str, str] = {}
        if self._output_locs:
            for v in self._output_locs:
                outputs[v.var] = self._interpolizer.interpolate(v.location, inputs=kwargs)

        if os.name == "nt":
            self._script = self._script.lstrip().rstrip().replace("\n", "&&")

        gen_script = self._interpolizer.interpolate(self._script, inputs=kwargs, outputs=outputs)
        if self._debug:
            print("\n==============================================\n")
            print(gen_script)
            print("\n==============================================\n")

        try:
            subprocess.check_call(gen_script, shell=True)
        except subprocess.CalledProcessError as e:
            files = os.listdir(".")
            fstr = "\n-".join(files)
            logger.error(
                f"Failed to Execute Script, return-code {e.returncode} \n"
                f"StdErr: {e.stderr}\n"
                f"StdOut: {e.stdout}\n"
                f" Current directory contents: .\n-{fstr}"
            )
            raise

        final_outputs = []
        for v in self._output_locs:
            if issubclass(v.var_type, FlyteFile):
                final_outputs.append(FlyteFile(outputs[v.var]))
            if issubclass(v.var_type, FlyteDirectory):
                final_outputs.append(FlyteDirectory(outputs[v.var]))
        if len(final_outputs) == 1:
            return final_outputs[0]
        if len(final_outputs) > 1:
            return tuple(final_outputs)
        return None

    def post_execute(self, user_params: ExecutionParameters, rval: typing.Any) -> typing.Any:
        return self._config_task_instance.post_execute(user_params, rval)
