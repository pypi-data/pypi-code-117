# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:53:55 2021

@author: jpeacock
"""
# =============================================================================
# Imports
# =============================================================================
import numpy as np
from xml.etree import cElementTree as et

from mt_metadata.base import Base

# =============================================================================


class TransferFunction(Base):
    """
    Deal with the complex XML format
    """

    def __init__(self):

        self.index_dict = {"hx": 0, "hy": 1, "ex": 0, "ey": 1, "hz": 0}
        self.dtype_dict = {
            "complex": complex,
            "real": float,
            "complex128": "complex",
            "float64": "real",
        }
        self.units_dict = {"z": "[mV/km]/[nT]", "t": "[]"}
        self.name_dict = {
            "exhx": "zxx",
            "exhy": "zxy",
            "eyhx": "zyx",
            "eyhy": "zyy",
            "hzhx": "tx",
            "hzhy": "ty",
        }

        self.period = None
        self.z = None
        self.z_var = None
        self.z_invsigcov = None
        self.z_residcov = None
        self.t = None
        self.t_var = None
        self.t_invsigcov = None
        self.t_residcov = None

        self.write_dict = {
            "z": {"out": {0: "ex", 1: "ey"}, "in": {0: "hx", 1: "hy"}},
            "z_var": {"out": {0: "ex", 1: "ey"}, "in": {0: "hx", 1: "hy"}},
            "z_invsigcov": {"out": {0: "hx", 1: "hy"}, "in": {0: "hx", 1: "hy"}},
            "z_residcov": {"out": {0: "ex", 1: "ey"}, "in": {0: "ex", 1: "ey"}},
            "t": {"out": {0: "hz"}, "in": {0: "hx", 1: "hy"}},
            "t_var": {"out": {0: "hz"}, "in": {0: "hx", 1: "hy"}},
            "t_invsigcov": {"out": {0: "hx", 1: "hy"}, "in": {0: "hx", 1: "hy"}},
            "t_residcov": {"out": {0: "hz"}, "in": {0: "hz"}},
        }

        super().__init__(attr_dict={})

    @property
    def period(self):
        """periods for estimates"""
        return self._period

    @period.setter
    def period(self, value):
        """
        Set the period, make sure the input is validated

        Linear period
        :param value: Linear period
        :type value: iterable

        """
        if value is None:
            self._period = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._period = np.array(value, dtype=float)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    @property
    def z(self):
        """zs for estimates"""
        return self._z

    @z.setter
    def z(self, value):
        """
        Set the z, make sure the input is validated

        """
        if value is None:
            self._z = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._z = np.array(value, dtype=complex)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    @property
    def z_var(self):
        """z_var for estimates"""
        return self._z_var

    @z_var.setter
    def z_var(self, value):
        """
        Set the z, make sure the input is validated

        """
        if value is None:
            self._z_var = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._z_var = np.array(value, dtype=float)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    @property
    def z_invsigcov(self):
        """z_invsigcov for estimates"""
        return self._z_invsigcov

    @z_invsigcov.setter
    def z_invsigcov(self, value):
        """
        Set the z, make sure the input is validated

        """
        if value is None:
            self._z_invsigcov = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._z_invsigcov = np.array(value, dtype=complex)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    @property
    def z_residcov(self):
        """z_residcov for estimates"""
        return self._z_residcov

    @z_residcov.setter
    def z_residcov(self, value):
        """
        Set the z, make sure the input is validated

        """
        if value is None:
            self._z_residcov = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._z_residcov = np.array(value, dtype=complex)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    @property
    def t(self):
        """ts for estimates"""
        return self._t

    @t.setter
    def t(self, value):
        """
        Set the t, make sure the input is validated

        """
        if value is None:
            self._t = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._t = np.array(value, dtype=complex)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    @property
    def t_var(self):
        """t_var for estimates"""
        return self._t_var

    @t_var.setter
    def t_var(self, value):
        """
        Set the t, make sure the input is validated

        """
        if value is None:
            self._t_var = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._t_var = np.array(value, dtype=float)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    @property
    def t_invsigcov(self):
        """t_invsigcov for estimates"""
        return self._t_invsigcov

    @t_invsigcov.setter
    def t_invsigcov(self, value):
        """
        Set the t, make sure the input is validated

        """
        if value is None:
            self._t_invsigcov = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._t_invsigcov = np.array(value, dtype=complex)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    @property
    def t_residcov(self):
        """t_residcov for estimates"""
        return self._t_residcov

    @t_residcov.setter
    def t_residcov(self, value):
        """
        Set the t, make sure the input is validated

        """
        if value is None:
            self._t_residcov = None

        elif isinstance(value, (list, tuple, np.ndarray)):
            self._t_residcov = np.array(value, dtype=complex)
        else:
            msg = (
                f"input values must be an list, tuple, or np.ndarray, not {type(value)}"
            )
            self.logger.error(msg)
            raise TypeError(msg)

    def initialize_arrays(self, n_periods):
        self._period = np.zeros(n_periods)
        self._z = np.zeros((n_periods, 2, 2), dtype=complex)
        self._z_var = np.zeros_like(self.z, dtype=float)
        self._z_invsigcov = np.zeros_like(self.z, dtype=complex)
        self._z_residcov = np.zeros_like(self.z, dtype=complex)
        self._t = np.zeros((n_periods, 1, 2), dtype=complex)
        self._t_var = np.zeros_like(self.t, dtype=float)
        self._t_invsigcov = np.zeros((n_periods, 2, 2), dtype=complex)
        self._t_residcov = np.zeros((n_periods, 1, 1), dtype=complex)

    @property
    def array_dict(self):
        return {
            "z": self.z,
            "z_var": self.z_var,
            "z_invsigcov": self.z_invsigcov,
            "z_residcov": self.z_residcov,
            "t": self.t,
            "t_var": self.t_var,
            "t_invsigcov": self.t_invsigcov,
            "t_residcov": self.t_residcov,
        }

    @property
    def n_periods(self):
        if self.period is not None:
            return self.period.size
        return 0

    def read_block(self, block, period_index):
        """
        Read a period block which is root_dict["data"]["period"][ii]

        :param block: DESCRIPTION
        :type block: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """
        for key in block.keys():
            comp = key.replace("_", "").replace(".", "_")
            if comp in ["value"]:
                continue
            try:
                dtype = self.dtype_dict[block[key]["type"]]
            except KeyError:
                dtype = float
            value_list = block[key]["value"]
            if not isinstance(value_list, list):
                value_list = [value_list]
            for item in value_list:
                index_0 = self.index_dict[item["output"].lower()]
                index_1 = self.index_dict[item["input"].lower()]
                if dtype is complex:
                    value = item["value"].split()
                    value = dtype(float(value[0]), float(value[1]))
                else:
                    value = dtype(item["value"])
                self.array_dict[comp][period_index, index_0, index_1] = value

    def read_data(self, root_dict):
        """
        read root_dict["data"]
        :param root_dict: DESCRIPTION
        :type root_dict: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """
        n_periods = int(float((root_dict["data"]["count"].strip())))
        self.initialize_arrays(n_periods)
        for ii, block in enumerate(root_dict["data"]["period"]):
            self.period[ii] = float(block["value"])
            self.read_block(block, ii)

    def write_block(self, parent, index):
        """
        Write a data block

        :param parent: DESCRIPTION
        :type parent: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """

        period_element = et.SubElement(
            parent, "Period", {"value": f"{self.period[index]:.6e}", "units": "secs"}
        )

        for key in self.array_dict.keys():
            if self.array_dict[key] is None:
                continue
            arr = self.array_dict[key][index]
            attr_dict = {
                "type": self.dtype_dict[arr.dtype.name],
                "size": str(arr.shape)[1:-1].replace(",", ""),
            }
            try:
                attr_dict["units"] = self.units_dict[key]
            except KeyError:
                pass

            comp_element = et.SubElement(
                period_element, key.replace("_", ".").upper(), attr_dict
            )
            idx_dict = self.write_dict[key]
            shape = arr.shape
            for ii in range(shape[0]):
                for jj in range(shape[1]):
                    ch_out = idx_dict["out"][ii]
                    ch_in = idx_dict["in"][jj]
                    a_dict = {}
                    try:
                        a_dict["name"] = self.name_dict[ch_out + ch_in].capitalize()
                    except KeyError:
                        pass
                    a_dict["output"] = ch_out.capitalize()
                    a_dict["input"] = ch_in.capitalize()
                    ch_element = et.SubElement(comp_element, "value", a_dict)
                    ch_value = f"{arr[ii, jj].real:.6e}"
                    if attr_dict["type"] in ["complex"]:
                        ch_value = f"{ch_value} {arr[ii, jj].imag:.6e}"
                    ch_element.text = ch_value

        return period_element

    def write_data(self, parent):
        """
        Write data blocks

        :param parent: DESCRIPTION
        :type parent: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """
        for index in range(self.period.size):
            self.write_block(parent, index)
