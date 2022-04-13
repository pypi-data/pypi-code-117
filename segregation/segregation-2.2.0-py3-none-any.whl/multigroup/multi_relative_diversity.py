"""Multigroup Relative Diversity index"""

__author__ = "Renan X. Cortes <renanc@ucr.edu>, Sergio J. Rey <sergio.rey@ucr.edu> and Elijah Knaap <elijah.knaap@ucr.edu>"

import numpy as np
from geopandas import GeoDataFrame

from .._base import MultiGroupIndex, SpatialImplicitIndex

np.seterr(divide="ignore", invalid="ignore")


def _multi_relative_diversity(data, groups):
    """
    Calculation of Multigroup Relative Diversity index

    Parameters
    ----------

    data   : a pandas DataFrame

    groups : list of strings.
             The variables names in data of the groups of interest of the analysis.

    Returns
    -------

    statistic : float
                Multigroup Relative Diversity Index

    core_data : a pandas DataFrame
                A pandas DataFrame that contains the columns used to perform the estimate.

    Notes
    -----
    Based on Reardon, Sean F. "Measures of racial diversity and segregation in multigroup and hierarchically structured populations." annual meeting of the Eastern Sociological Society, Philadelphia, PA. 1998.

    High diversity means less segregation.

    Reference: :cite:`reardon1998measures`.

    """

    core_data = data[groups]
    df = np.array(core_data)

    T = df.sum()

    ti = df.sum(axis=1)
    pik = df / ti[:, None]
    pik = np.nan_to_num(pik)  # Replace NaN from zerodivision when unit has no population
    Pk = df.sum(axis=0) / df.sum()
    Is = (Pk * (1 - Pk)).sum()

    MRD = (ti[:, None] * (pik - Pk) ** 2).sum() / (T * Is)
    if isinstance(data, GeoDataFrame):
        core_data = data[[data.geometry.name]].join(core_data)
    return MRD, core_data, groups


class MultiRelativeDiversity(MultiGroupIndex, SpatialImplicitIndex):
    """Multigroup Relative Diversity Index.

    Parameters
    ----------
    data : pandas.DataFrame or geopandas.GeoDataFrame, required
        dataframe or geodataframe if spatial index holding data for location of interest
    groups : list, required
        list of columns on dataframe holding population totals for each group
    w : libpysal.weights.KernelW, optional
        lipysal spatial kernel weights object used to define an egohood
    network : pandana.Network
        pandana Network object representing the study area
    distance : int
        Maximum distance (in units of geodataframe CRS) to consider the extent of the egohood
    decay : str
        type of decay function to apply. Options include
    precompute : bool
        Whether to precompute the pandana Network object

    Attributes
    ----------
    statistic : float
        Multigroup Dissimilarity Index value
    core_data : a pandas DataFrame
        DataFrame that contains the columns used to perform the estimate.

    Notes
    -----
    Based on Reardon, Sean F., and Glenn Firebaugh. "Measures of multigroup segregation." Sociological methodology 32.1 (2002): 33-67.

    Reference: :cite:`reardon2002measures`.
    """

    def __init__(
        self,
        data,
        groups,
        w=None,
        network=None,
        distance=None,
        decay=None,
        precompute=None,
        function='triangular',
        **kwargs
    ):
        """Init."""
        MultiGroupIndex.__init__(self, data, groups)
        if any([w, network, distance]):
            SpatialImplicitIndex.__init__(self, w, network, distance, decay, function, precompute)
        aux = _multi_relative_diversity(self.data, self.groups)

        self.statistic = aux[0]
        self.data = aux[1]
        self.groups = aux[2]
        self._function = _multi_relative_diversity
