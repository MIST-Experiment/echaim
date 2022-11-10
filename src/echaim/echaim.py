import os
from ctypes import *
from datetime import datetime

import numpy as np
from time import time

c_double_p = POINTER(c_double)
c_int_p = POINTER(c_int)

echaim_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "source_c/cmake-build-debug"
)
echaim = np.ctypeslib.load_library("libECHAIM", echaim_path)


def density_profile(lats: np.ndarray, lons: np.ndarray, dt: datetime, alts: np.ndarray, storm: bool = True,
                    precip: bool = True, dregion: bool = True):
    if alts.ndim != 1:
        raise ValueError("Array of altitudes must be 1D")
    l1 = c_int(len(alts))
    l0 = c_int(len(lats))
    alts_p = alts.ctypes.data_as(c_double_p)
    lats_p = lats.ctypes.data_as(c_double_p)
    lons_p = lons.ctypes.data_as(c_double_p)

    datadir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "model_data/")

    output = np.empty(len(alts), dtype=np.float64)
    output_p = output.ctypes.data_as(c_double_p)

    t1 = time()
    # echaim.pyDensityProfile(output_p, datadir.encode("utf-8"),
    #                         lats_p, lons_p,
    #                         c_int(dt.year), c_int(dt.month), c_int(dt.day),
    #                         c_int(dt.hour), c_int(dt.minute), c_int(dt.second),
    #                         c_int(storm), c_int(precip), c_int(dregion),
    #                         l0, alts_p, l1, c_int(0))
    year_p = np.array([dt.year]*len(lats), dtype=np.int32).ctypes.data_as(c_int_p)
    month_p = np.array([dt.month]*len(lats)).ctypes.data_as(c_int_p)
    day_p = np.array([dt.day]*len(lats)).ctypes.data_as(c_int_p)
    hour_p = np.array([dt.hour]*len(lats)).ctypes.data_as(c_int_p)
    minute_p = np.array([dt.minute]*len(lats)).ctypes.data_as(c_int_p)
    second_p = np.array([dt.second]*len(lats)).ctypes.data_as(c_int_p)
    echaim.pyDensityProfile(output_p, datadir.encode("utf-8"),
                            lats_p, lons_p,
                            year_p, month_p, day_p,
                            hour_p, minute_p, second_p,
                            c_int(storm), c_int(precip), c_int(dregion),
                            l0, alts_p, l1, c_int(0))
    print(f"Run time:\t{time() - t1:.2f}s")
    return output
