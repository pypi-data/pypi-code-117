# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_model.ipynb (unless otherwise specified).

__all__ = ['BaseModel', 'DirectoryModel', 'SingleModel', 'WandbKerasModel', 'ExternalCSVs', 'NumerBayCSVs',
           'JoblibModel', 'CatBoostModel', 'LGBMModel', 'ConstantModel', 'RandomModel', 'ExamplePredictionsModel',
           'AwesomeModel', 'AwesomeDirectoryModel']

# Cell
import os
import gc
import uuid
import wandb
import joblib
import pickle
import numpy as np
import pandas as pd
import lightgbm as lgb
import tensorflow as tf
from pathlib import Path
from typing import Union
from tqdm.auto import tqdm
from functools import partial
from catboost import CatBoost
from numerbay import NumerBay
from typeguard import typechecked
from abc import ABC, abstractmethod
from rich import print as rich_print
from sklearn.dummy import DummyRegressor

from .download import NumeraiClassicDownloader
from .numerframe import NumerFrame, create_numerframe
from .preprocessing import display_processor_info

# Cell
class BaseModel(ABC):
    """
    Setup for model prediction on a Dataset.

    :param model_directory: Main directory from which to read in models. \n
    :param model_name: Name that will be used to create column names and for display purposes.
    """
    def __init__(self, model_directory: str,
                 model_name: str = None,
                 ):
        self.model_directory = Path(model_directory)
        self.model_name = model_name if model_name else uuid.uuid4().hex
        self.prediction_col_name = f"prediction_{self.model_name}"
        self.description = f"{self.__class__.__name__}: '{self.model_name}' prediction"

    @abstractmethod
    def predict(self, dataf: Union[pd.DataFrame, NumerFrame]) -> NumerFrame:
        """ Return NumerFrame with column added for prediction. """
        ...
        return NumerFrame(dataf)

    def get_prediction_col_names(self, pred_shape: tuple) -> list:
        """ Create multiple columns if predictions are multi-target. """
        prediction_cols = self.prediction_col_name
        if len(pred_shape) > 1:
            if pred_shape[1] > 1:
                prediction_cols = [f"{self.prediction_col_name}_{i}" for i in range(pred_shape[1])]
        return prediction_cols

    def __call__(self, dataf: Union[pd.DataFrame, NumerFrame]) -> NumerFrame:
        return self.predict(dataf=dataf)

# Cell
class DirectoryModel(BaseModel):
    """
    Base class implementation where predictions are averaged out from a directory of models. Walks through every file with given file_suffix in a directory.

    :param model_directory: Main directory from which to read in models. \n
    :param file_suffix: File format to load (For example, .joblib, .pkl, .cbm or .lgb) \n
    :param model_name: Name that will be used to create column names and for display purposes. \n
    :param feature_cols: optional list of features to use for prediction. Selects all feature columns (i.e. column names with prefix 'feature') by default. \n
    :param combine_preds: Whether to average predictions along column axis. Only relevant for multi target models. \n
    Convenient when you want to predict the main target by averaging a multi-target model.
    """
    def __init__(self, model_directory: str, file_suffix: str,
                 model_name: str = None,
                 feature_cols: list = None,
                 combine_preds = True,
                 ):
        super().__init__(model_directory=model_directory,
                         model_name=model_name,
                         )
        self.file_suffix = file_suffix
        self.model_paths = list(self.model_directory.glob(f'*.{self.file_suffix}'))
        if self.file_suffix:
            assert self.model_paths, f"No {self.file_suffix} files found in {self.model_directory}."
        self.total_models = len(self.model_paths)
        self.feature_cols = feature_cols
        self.combine_preds = combine_preds

    @display_processor_info
    def predict(self, dataf: NumerFrame, *args, **kwargs) -> NumerFrame:
        """
        Use all recognized models to make predictions and average them out.
        :param dataf: A Preprocessed DataFrame where all its features can be passed to the model predict method.
        *args, **kwargs will be parsed into the model.predict method.
        :return: A new dataset with prediction column added.
        """
        dataf.loc[:, self.prediction_col_name] = np.zeros(len(dataf))
        models = self.load_models()
        feature_cols = self.feature_cols if self.feature_cols else dataf.feature_cols
        for model in tqdm(models, desc=self.description, position=1):
            predictions = model.predict(dataf[feature_cols], *args, **kwargs)
            # Check for if model output is a Pandas DataFrame
            predictions = predictions.values if isinstance(predictions, pd.DataFrame) else predictions
            predictions = predictions.mean(axis=1) if self.combine_preds and len(predictions.shape) > 1 else predictions
            prediction_cols = self.get_prediction_col_names(predictions.shape)
            dataf.loc[:, prediction_cols] = dataf.loc[:, prediction_cols] + (predictions / self.total_models)
        del models; gc.collect()
        return NumerFrame(dataf)

    @abstractmethod
    def load_models(self) -> list:
        """ Instantiate all models detected in self.model_paths. """
        ...

# Cell
@typechecked
class SingleModel(BaseModel):
    """
    Load single model from file and perform prediction logic.

    :param model_file_path: Full path to model file. \n
    :param model_name: Name that will be used to create column names and for display purposes. \n
    :param combine_preds: Whether to average predictions along column axis. Only relevant for multi target models.
    Convenient when you want to predict the main target by averaging a multi-target model. \n
    :param autoencoder_mlp: Whether your model is an autoencoder + MLP model.
    Will take the 3rd of tuple output in this case. Only relevant for NN models.
    More info on autoencoders:
    https://forum.numer.ai/t/autoencoder-and-multitask-mlp-on-new-dataset-from-kaggle-jane-street/4338 \n
    :param feature_cols: optional list of features to use for prediction. Selects all feature columns (i.e. column names with prefix 'feature') by default.
    """
    def __init__(self, model_file_path: str, model_name: str = None,
                 combine_preds = False, autoencoder_mlp = False,
                 feature_cols: list = None
                 ):
        self.model_file_path = Path(model_file_path)
        assert self.model_file_path.exists(), f"File path '{self.model_file_path}' does not exist."
        assert self.model_file_path.is_file(), f"File path must point to file. Not valid for '{self.model_file_path}'."
        super().__init__(model_directory=str(self.model_file_path.parent),
                         model_name=model_name,
                         )
        self.model_suffix = self.model_file_path.suffix
        self.suffix_to_model_mapping = {".joblib": joblib.load,
                                        ".cbm": CatBoost().load_model,
                                        ".pkl": pickle.load,
                                        ".pickle": pickle.load,
                                        ".h5": partial(tf.keras.models.load_model, compile=False)
                                        }
        self.__check_valid_suffix()
        self.combine_preds = combine_preds
        self.autoencoder_mlp = autoencoder_mlp
        self.feature_cols = feature_cols

    def predict(self, dataf: NumerFrame, *args, **kwargs) -> NumerFrame:
        model = self._load_model(*args, **kwargs)
        feature_cols = self.feature_cols if self.feature_cols else dataf.feature_cols
        predictions = model.predict(dataf[feature_cols])
        # Check for if model output is a Pandas DataFrame
        predictions = predictions.values if isinstance(predictions, pd.DataFrame) else predictions
        predictions = predictions[2] if self.autoencoder_mlp else predictions
        predictions = predictions.mean(axis=1) if self.combine_preds else predictions
        prediction_cols = self.get_prediction_col_names(predictions.shape)
        dataf.loc[:, prediction_cols] = predictions
        del model; gc.collect()
        return NumerFrame(dataf)

    def _load_model(self, *args, **kwargs):
        """ Load arbitrary model from path using suffix to model mapping. """
        return self.suffix_to_model_mapping[self.model_suffix](str(self.model_file_path), *args, **kwargs)

    def __check_valid_suffix(self):
        """ Detailed message if model is not supported in this class. """
        try:
            self.suffix_to_model_mapping[self.model_suffix]
        except KeyError:
            raise NotImplementedError(
                f"Format '{self.model_suffix}' is not available. Available versions are {list(self.suffix_to_model_mapping.keys())}"
            )


# Cell
@typechecked
class WandbKerasModel(SingleModel):
    """
    Download best .h5 model from Weights & Biases (W&B) run in local directory and make predictions.
    More info on W&B: https://wandb.ai/site

    :param run_path: W&B path structured as entity/project/run_id.
    Can be copied from the Overview tab of a W&B run.
    For more info: https://docs.wandb.ai/ref/app/pages/run-page#overview-tab \n
    :param file_name: Name of .h5 file as saved in W&B run.
    'model-best.h5' by default.
    File name can be found under files tab of W&B run. \n
    :param combine_preds: Whether to average predictions along column axis. Convenient when you want to predict the main target by averaging a multi-target model. \n
    :param autoencoder_mlp: Whether your model is an autoencoder + MLP model.
    Will take the 3rd of tuple output in this case. Only relevant for NN models. \n
    More info on autoencoders:
    https://forum.numer.ai/t/autoencoder-and-multitask-mlp-on-new-dataset-from-kaggle-jane-street/4338 \n
    :param replace: Replace any model files saved under the same file name with downloaded W&B run model. WARNING: Setting to True may overwrite models in your local environment. \n
    :param feature_cols: optional list of features to use for prediction. Selects all feature columns (i.e. column names with prefix 'feature') by default.
    """
    def __init__(self,
                 run_path: str,
                 file_name: str = "model-best.h5",
                 combine_preds = False,
                 autoencoder_mlp = False,
                 replace = False,
                 feature_cols: list = None
                 ):
        self.run_path = run_path
        self.file_name = file_name
        self.replace = replace

        self._download_model()
        super().__init__(model_file_path=f"{self.run_path.split('/')[-1]}_{self.file_name}",
                         model_name=self.run_path,
                         combine_preds=combine_preds,
                         autoencoder_mlp=autoencoder_mlp,
                         feature_cols=feature_cols
                         )

    def _download_model(self):
        """
        Use W&B API to download .h5 model file.
        More info on API: https://docs.wandb.ai/guides/track/public-api-guide
        """
        if Path(self.file_name).is_file() and not self.replace:
            rich_print(f":warning: [red] Model file '{self.file_name}' already exists in local environment.\
            Skipping download of W&B run model. If this is not the model you want to use for prediction\
            consider moving it or set 'replace=True' at initialization to overwrite. [/red] :warning:")
        else:
            rich_print(f":page_facing_up: [green] Downloading '{self.file_name}' from '{self.run_path}' in W&B Cloud. [/green] :page_facing_up:")
        run = wandb.Api().run(self.run_path)
        run.file(name=self.file_name).download(replace=self.replace)
        os.rename(self.file_name, f"{self.run_path.split('/')[-1]}_{self.file_name}")

# Cell
@typechecked
class ExternalCSVs(BaseModel):
    """
    Load external submissions and add to NumerFrame. \n
    All csv files in this directory will be added to NumerFrame.
    Make sure all external predictions are prepared and ready for submission. i.e. IDs lining up and one column named 'prediction'. \n
    :param data_directory: Directory path for retrieving external submission.
    """
    def __init__(self, data_directory: str = "external_submissions"):
        super().__init__(model_directory=data_directory)
        self.data_directory = Path(data_directory)
        self.paths = list(self.data_directory.glob("*.csv"))
        if not self.paths:
            rich_print(f":warning: WARNING: No csvs found in directory '{self.data_directory}'. :warning:")

    def predict(self, dataf: NumerFrame) -> NumerFrame:
        """ Return NumerFrame with added external predictions. """
        for path in tqdm(self.paths, desc="External submissions"):
            dataf.loc[:, f"prediction_{path.name}"] = self._get_preds(path)
        return NumerFrame(dataf)

    def _get_preds(self, path: Path) -> pd.Series:
        pred_col = pd.read_csv(path, index_col=0, header=0)['prediction']
        if not pred_col.between(0, 1).all():
            raise ValueError(f"Prediction values must be between 0 and 1. Does not hold for '{path.name}'.")
        return pred_col

# Cell
@typechecked
class NumerBayCSVs(BaseModel):
    """
    Load NumerBay submissions and add to NumerFrame. \n
    Make sure to provide correct NumerBay credentials and that your purchases have been confirmed and artifacts are available for download. \n
    :param data_directory: Directory path for caching submission. Files not already present in the directory will be downloaded from NumerBay.
    :param numerbay_product_full_names: List of product full names (in the format of [category]-[product name]) to download from NumerBay. E.g. ['numerai-predictions-numerbay']
    :param numerbay_username: NumerBay username
    :param numerbay_password: NumerBay password
    :param numerbay_key_path: NumerBay encryption key json file path (exported from the profile page)

    """
    def __init__(self,
                 data_directory: str = "numerbay_submissions",
                 numerbay_product_full_names: list = None,
                 numerbay_username: str = None,
                 numerbay_password: str = None,
                 numerbay_key_path: str = None,
                 ticker_col: str = 'bloomberg_ticker'):
        super().__init__(model_directory=data_directory)
        self.data_directory = Path(data_directory)
        self.numerbay_product_full_names = numerbay_product_full_names
        self.numerbay_key_path = numerbay_key_path
        self._api = None
        self._get_api_func = lambda: NumerBay(username=numerbay_username, password=numerbay_password)
        self.ticker_col = ticker_col
        self.classic_number = 8
        self.signals_number = 11

    def predict(self, dataf: NumerFrame) -> NumerFrame:
        """ Return NumerFrame with added NumerBay predictions. """
        for numerbay_product_full_name in tqdm(self.numerbay_product_full_names, desc="NumerBay submissions"):
            pred_name = f"prediction_{numerbay_product_full_name}"
            if dataf.meta.era_col == "era":
                dataf.loc[:, pred_name] = \
                    self._get_preds(numerbay_product_full_name, tournament=self.classic_number)
            else:
                dataf.loc[:, pred_name] = \
                    dataf.merge(self._get_preds(numerbay_product_full_name, tournament=self.signals_number),
                                on=[self.ticker_col, dataf.meta.era_col], how='left')['signal']
        return NumerFrame(dataf)

    @property
    def api(self):
        if self._api is None:
            self._api = self._get_api_func()
        return self._api

    def _get_preds(self, numerbay_product_full_name: str, tournament: int) -> pd.Series:
        if tournament == self.signals_number: # Temporarily disable Signals
            raise NotImplementedError("NumerBay Signals predictions not yet supported.")

        # Scan for already downloaded files, allows arbitrary ext just in case (e.g. csv.zip)
        file_paths = list(self.data_directory.glob(f"{numerbay_product_full_name}.*"))
        if len(file_paths) > 0:
            file_path = file_paths[0]
        else:
            file_path = Path.joinpath(self.data_directory, f"{numerbay_product_full_name}.csv")

        # Download file if needed
        if not file_path.is_file():
            # Download to a tmp file
            tmp_path = Path.joinpath(self.data_directory, f".{numerbay_product_full_name}.tmp")
            self.api.download_artifact(
                dest_path=str(tmp_path),
                product_full_name=numerbay_product_full_name,
                key_path=self.numerbay_key_path
            )
            # Rename file after successful download (and decryption)
            os.rename(tmp_path, file_path)

        # Read downloaded file
        if file_path.is_file():
            if tournament == self.classic_number:
                pred_col = pd.read_csv(file_path, index_col=0, header=0)['prediction']
            elif tournament == self.signals_number:
                pass
            else:
                raise ValueError(f"Invalid tournament '{tournament}'.")
        else:
            raise FileNotFoundError(f"No file found in directory '{self.data_directory}' for NumerBay product "
                                    f"'{numerbay_product_full_name}'.")

        # validity check
        if not pred_col.between(0, 1).all():
            raise ValueError(f"Prediction values must be between 0 and 1. Does not hold for '{path.name}'.")
        return pred_col

# Cell
@typechecked
class JoblibModel(DirectoryModel):
    """
    Load and predict for arbitrary models in directory saved as .joblib.

    All loaded models should have a .predict method and accept the features present in the data.

    :param model_directory: Main directory from which to read in models. \n
    :param model_name: Name that will be used to create column names and for display purposes. \n
    :param feature_cols: optional list of features to use for prediction. Selects all feature columns (i.e. column names with prefix 'feature') by default.
    """
    def __init__(self,
                 model_directory: str,
                 model_name: str = None,
                 feature_cols: list = None
                 ):
        file_suffix = 'joblib'
        super().__init__(model_directory=model_directory,
                         file_suffix=file_suffix,
                         model_name=model_name,
                         feature_cols=feature_cols
                         )

    def load_models(self) -> list:
        return [joblib.load(path) for path in self.model_paths]

# Cell
@typechecked
class CatBoostModel(DirectoryModel):
    """
    Load and predict with all .cbm models (CatBoostRegressor) in directory.

    :param model_directory: Main directory from which to read in models. \n
    :param model_name: Name that will be used to define column names and for display purposes. \n
    :param feature_cols: optional list of features to use for prediction. Selects all feature columns (i.e. column names with prefix 'feature') by default.
    """
    def __init__(self,
                 model_directory: str,
                 model_name: str = None,
                 feature_cols: list = None
                 ):
        file_suffix = 'cbm'
        super().__init__(model_directory=model_directory,
                         file_suffix=file_suffix,
                         model_name=model_name,
                         feature_cols=feature_cols
                         )

    def load_models(self) -> list:
        return [CatBoost().load_model(path) for path in self.model_paths]

# Cell
@typechecked
class LGBMModel(DirectoryModel):
    """
    Load and predict with all .lgb models (LightGBM) in directory.

    :param model_directory: Main directory from which to read in models. \n
    :param model_name: Name that will be used to define column names and for display purposes. \n
    :param feature_cols: optional list of features to use for prediction. Selects all feature columns (i.e. column names with prefix 'feature') by default.
    """
    def __init__(self,
                 model_directory: str,
                 model_name: str = None,
                 feature_cols: list = None
                 ):
        file_suffix = 'lgb'
        super().__init__(model_directory=model_directory,
                         file_suffix=file_suffix,
                         model_name=model_name,
                         feature_cols=feature_cols
                         )

    def load_models(self) -> list:
        return [lgb.Booster(model_file=str(path)) for path in self.model_paths]

# Cell
class ConstantModel(BaseModel):
    """
    WARNING: Only use this Model for testing purposes. \n
    Create constant prediction.

    :param constant: Value for constant prediction. \n
    :param model_name: Name that will be used to create column names and for display purposes.
    """
    def __init__(self, constant: float = 0.5, model_name: str = None):
        self.constant = constant
        model_name = model_name if model_name else f"constant_{self.constant}"
        super().__init__(model_directory="",
                         model_name=model_name
                         )
        self.clf = DummyRegressor(strategy='constant', constant=constant).fit([0.], [0.])

    def predict(self, dataf: NumerFrame) -> NumerFrame:
        dataf.loc[:, self.prediction_col_name] = self.clf.predict(dataf.get_feature_data)
        return NumerFrame(dataf)

# Cell
class RandomModel(BaseModel):
    """
    WARNING: Only use this Model for testing purposes. \n
    Create uniformly distributed predictions.

    :param model_name: Name that will be used to create column names and for display purposes.
    """
    def __init__(self, model_name: str = None):
        model_name = model_name if model_name else "random"
        super().__init__(model_directory="",
                         model_name=model_name
                         )

    def predict(self, dataf: Union[pd.DataFrame, NumerFrame]) -> NumerFrame:
        dataf.loc[:, self.prediction_col_name] = np.random.uniform(size=len(dataf))
        return NumerFrame(dataf)

# Cell
@typechecked
class ExamplePredictionsModel(BaseModel):
    """
    Load example predictions and add to NumerFrame. \n
    :param file_name: File to download from NumerAPI.
    'example_validation_predictions.parquet' by default. \n
    :param data_directory: Directory path to download example predictions to or directory where example data already exists. \n
    :param round_num: Optional round number. Downloads most recent round by default.
    """
    def __init__(self, file_name: str = "example_validation_predictions.parquet",
                 data_directory: str = "example_predictions_model",
                 round_num: int = None):
        super().__init__(model_directory="",
                         model_name="example",
                         )
        self.file_name = file_name
        self.data_directory = data_directory
        self.round_num = round_num

    @display_processor_info
    def predict(self, dataf: NumerFrame) -> NumerFrame:
        """ Return NumerFrame with added example predictions. """
        self._download_example_preds()
        example_preds = self._load_example_preds()
        dataf.loc[:, self.prediction_col_name] = dataf.merge(example_preds, on='id', how='left')['prediction']
        self.downloader.remove_base_directory()
        return NumerFrame(dataf)

    def _download_example_preds(self):
        self.downloader = NumeraiClassicDownloader(directory_path=self.data_directory)
        self.dest_path = f"{str(self.downloader.dir)}/{self.file_name}"
        self.downloader.download_single_dataset(filename=self.file_name,
                                                dest_path=self.dest_path,
                                                round_num=self.round_num)

    def _load_example_preds(self, *args, **kwargs):
        return pd.read_parquet(self.dest_path, *args, **kwargs)

# Cell
@typechecked
class AwesomeModel(BaseModel):
    """
    TEMPLATE - Predict with arbitrary prediction logic and model formats.

    :param model_directory: Main directory from which to read in models. \n
    :param model_name: Name that will be used to define column names and for display purposes. \n
    :param feature_cols: optional list of features to use for prediction. Selects all feature columns (i.e. column names with prefix 'feature') by default.
    """
    def __init__(self, model_directory: str, model_name: str = None,
                 feature_cols: list = None):
        super().__init__(model_directory=model_directory,
                         model_name=model_name,
                         )
        self.feature_cols = feature_cols

    @display_processor_info
    def predict(self, dataf: NumerFrame) -> NumerFrame:
        """ Return NumerFrame with column(s) added for prediction(s). """
        # Get all features
        feature_cols = self.feature_cols if self.feature_cols else dataf.feature_cols
        feature_df = dataf[feature_cols]
        # Predict and add to new column
        ...
        # Parse all contents of NumerFrame to the next pipeline step
        return NumerFrame(dataf)

# Cell
@typechecked
class AwesomeDirectoryModel(DirectoryModel):
    """
    TEMPLATE - Load in all models of arbitrary file format and predict for all.

    :param model_directory: Main directory from which to read in models. \n
    :param model_name: Name that will be used to define column names and for display purposes. \n
    :param feature_cols: optional list of features to use for prediction. Selects all feature columns (i.e. column names with prefix 'feature') by default.
    """
    def __init__(self,
                 model_directory: str,
                 model_name: str = None,
                 feature_cols: list = None
                 ):
        file_suffix = '.anything'
        super().__init__(model_directory=model_directory,
                         file_suffix=file_suffix,
                         model_name=model_name,
                         feature_cols=feature_cols
                         )

    def load_models(self) -> list:
        """ Instantiate all models and return as a list. (abstract method) """
        ...