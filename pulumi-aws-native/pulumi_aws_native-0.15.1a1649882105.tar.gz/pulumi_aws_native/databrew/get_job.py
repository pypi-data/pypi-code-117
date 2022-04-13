# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetJobResult',
    'AwaitableGetJobResult',
    'get_job',
    'get_job_output',
]

@pulumi.output_type
class GetJobResult:
    def __init__(__self__, data_catalog_outputs=None, database_outputs=None, dataset_name=None, encryption_key_arn=None, encryption_mode=None, job_sample=None, log_subscription=None, max_capacity=None, max_retries=None, output_location=None, outputs=None, profile_configuration=None, project_name=None, recipe=None, role_arn=None, timeout=None, validation_configurations=None):
        if data_catalog_outputs and not isinstance(data_catalog_outputs, list):
            raise TypeError("Expected argument 'data_catalog_outputs' to be a list")
        pulumi.set(__self__, "data_catalog_outputs", data_catalog_outputs)
        if database_outputs and not isinstance(database_outputs, list):
            raise TypeError("Expected argument 'database_outputs' to be a list")
        pulumi.set(__self__, "database_outputs", database_outputs)
        if dataset_name and not isinstance(dataset_name, str):
            raise TypeError("Expected argument 'dataset_name' to be a str")
        pulumi.set(__self__, "dataset_name", dataset_name)
        if encryption_key_arn and not isinstance(encryption_key_arn, str):
            raise TypeError("Expected argument 'encryption_key_arn' to be a str")
        pulumi.set(__self__, "encryption_key_arn", encryption_key_arn)
        if encryption_mode and not isinstance(encryption_mode, str):
            raise TypeError("Expected argument 'encryption_mode' to be a str")
        pulumi.set(__self__, "encryption_mode", encryption_mode)
        if job_sample and not isinstance(job_sample, dict):
            raise TypeError("Expected argument 'job_sample' to be a dict")
        pulumi.set(__self__, "job_sample", job_sample)
        if log_subscription and not isinstance(log_subscription, str):
            raise TypeError("Expected argument 'log_subscription' to be a str")
        pulumi.set(__self__, "log_subscription", log_subscription)
        if max_capacity and not isinstance(max_capacity, int):
            raise TypeError("Expected argument 'max_capacity' to be a int")
        pulumi.set(__self__, "max_capacity", max_capacity)
        if max_retries and not isinstance(max_retries, int):
            raise TypeError("Expected argument 'max_retries' to be a int")
        pulumi.set(__self__, "max_retries", max_retries)
        if output_location and not isinstance(output_location, dict):
            raise TypeError("Expected argument 'output_location' to be a dict")
        pulumi.set(__self__, "output_location", output_location)
        if outputs and not isinstance(outputs, list):
            raise TypeError("Expected argument 'outputs' to be a list")
        pulumi.set(__self__, "outputs", outputs)
        if profile_configuration and not isinstance(profile_configuration, dict):
            raise TypeError("Expected argument 'profile_configuration' to be a dict")
        pulumi.set(__self__, "profile_configuration", profile_configuration)
        if project_name and not isinstance(project_name, str):
            raise TypeError("Expected argument 'project_name' to be a str")
        pulumi.set(__self__, "project_name", project_name)
        if recipe and not isinstance(recipe, dict):
            raise TypeError("Expected argument 'recipe' to be a dict")
        pulumi.set(__self__, "recipe", recipe)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if timeout and not isinstance(timeout, int):
            raise TypeError("Expected argument 'timeout' to be a int")
        pulumi.set(__self__, "timeout", timeout)
        if validation_configurations and not isinstance(validation_configurations, list):
            raise TypeError("Expected argument 'validation_configurations' to be a list")
        pulumi.set(__self__, "validation_configurations", validation_configurations)

    @property
    @pulumi.getter(name="dataCatalogOutputs")
    def data_catalog_outputs(self) -> Optional[Sequence['outputs.JobDataCatalogOutput']]:
        return pulumi.get(self, "data_catalog_outputs")

    @property
    @pulumi.getter(name="databaseOutputs")
    def database_outputs(self) -> Optional[Sequence['outputs.JobDatabaseOutput']]:
        return pulumi.get(self, "database_outputs")

    @property
    @pulumi.getter(name="datasetName")
    def dataset_name(self) -> Optional[str]:
        """
        Dataset name
        """
        return pulumi.get(self, "dataset_name")

    @property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[str]:
        """
        Encryption Key Arn
        """
        return pulumi.get(self, "encryption_key_arn")

    @property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional['JobEncryptionMode']:
        """
        Encryption mode
        """
        return pulumi.get(self, "encryption_mode")

    @property
    @pulumi.getter(name="jobSample")
    def job_sample(self) -> Optional['outputs.JobSample']:
        """
        Job Sample
        """
        return pulumi.get(self, "job_sample")

    @property
    @pulumi.getter(name="logSubscription")
    def log_subscription(self) -> Optional['JobLogSubscription']:
        """
        Log subscription
        """
        return pulumi.get(self, "log_subscription")

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[int]:
        """
        Max capacity
        """
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[int]:
        """
        Max retries
        """
        return pulumi.get(self, "max_retries")

    @property
    @pulumi.getter(name="outputLocation")
    def output_location(self) -> Optional['outputs.JobOutputLocation']:
        """
        Output location
        """
        return pulumi.get(self, "output_location")

    @property
    @pulumi.getter
    def outputs(self) -> Optional[Sequence['outputs.JobOutput']]:
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter(name="profileConfiguration")
    def profile_configuration(self) -> Optional['outputs.JobProfileConfiguration']:
        """
        Profile Job configuration
        """
        return pulumi.get(self, "profile_configuration")

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[str]:
        """
        Project name
        """
        return pulumi.get(self, "project_name")

    @property
    @pulumi.getter
    def recipe(self) -> Optional['outputs.JobRecipe']:
        return pulumi.get(self, "recipe")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        Role arn
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def timeout(self) -> Optional[int]:
        """
        Timeout
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="validationConfigurations")
    def validation_configurations(self) -> Optional[Sequence['outputs.JobValidationConfiguration']]:
        """
        Data quality rules configuration
        """
        return pulumi.get(self, "validation_configurations")


class AwaitableGetJobResult(GetJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobResult(
            data_catalog_outputs=self.data_catalog_outputs,
            database_outputs=self.database_outputs,
            dataset_name=self.dataset_name,
            encryption_key_arn=self.encryption_key_arn,
            encryption_mode=self.encryption_mode,
            job_sample=self.job_sample,
            log_subscription=self.log_subscription,
            max_capacity=self.max_capacity,
            max_retries=self.max_retries,
            output_location=self.output_location,
            outputs=self.outputs,
            profile_configuration=self.profile_configuration,
            project_name=self.project_name,
            recipe=self.recipe,
            role_arn=self.role_arn,
            timeout=self.timeout,
            validation_configurations=self.validation_configurations)


def get_job(name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobResult:
    """
    Resource schema for AWS::DataBrew::Job.


    :param str name: Job name
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:databrew:getJob', __args__, opts=opts, typ=GetJobResult).value

    return AwaitableGetJobResult(
        data_catalog_outputs=__ret__.data_catalog_outputs,
        database_outputs=__ret__.database_outputs,
        dataset_name=__ret__.dataset_name,
        encryption_key_arn=__ret__.encryption_key_arn,
        encryption_mode=__ret__.encryption_mode,
        job_sample=__ret__.job_sample,
        log_subscription=__ret__.log_subscription,
        max_capacity=__ret__.max_capacity,
        max_retries=__ret__.max_retries,
        output_location=__ret__.output_location,
        outputs=__ret__.outputs,
        profile_configuration=__ret__.profile_configuration,
        project_name=__ret__.project_name,
        recipe=__ret__.recipe,
        role_arn=__ret__.role_arn,
        timeout=__ret__.timeout,
        validation_configurations=__ret__.validation_configurations)


@_utilities.lift_output_func(get_job)
def get_job_output(name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJobResult]:
    """
    Resource schema for AWS::DataBrew::Job.


    :param str name: Job name
    """
    ...
