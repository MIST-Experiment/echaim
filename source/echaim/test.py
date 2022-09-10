from ctypes import *

import numpy as np

c_double_p = POINTER(c_double)
c_int_p = POINTER(c_int)

echaim = np.ctypeslib.load_library("libECHAIM", "../../")

from tqdm import tqdm

# lat = np.array([79.4153203], dtype=np.float64).ctypes.data_as(c_double_p)
lat = c_double(79.4153203)
lon = c_double(-90.7513825)
year = c_int(2022)
month = c_int(7)
day = c_int(17)
hour = c_int(12)
minute = c_int(0)
second = c_int(0)

storm = c_int(1)
precip = c_int(1)
dregion = c_int(1)

altProfile = np.concatenate([
    np.arange(60, 91, 1, dtype=np.float64),
    np.arange(150, 501, 5, dtype=np.float64),
])

l1 = c_int(len(altProfile))
altProfile_p = altProfile.ctypes.data_as(c_double_p)
output = np.empty(len(altProfile), dtype=np.float64)
output_p = output.ctypes.data_as(c_double_p)

lats = np.linspace(50, 90, 41)
lons = np.linspace(0, 360, 61)

lats_m, lons_m = np.meshgrid(lats, lons)
lats_f = lats_m.flatten()
lons_f = lons_m.flatten()

res = np.zeros((len(lons_f), len(altProfile)), dtype=np.float64)

for i in tqdm(range(len(lats_f))):
    echaim.pyDensityProfile(output_p, c_double(lats_f[i]), c_double(lons_f[i]), year, month, day, hour, minute, second,
                            storm, precip, dregion, altProfile_p, l1, c_int(0))
    res[i][:] = output[:]

np.save("echaim", res.reshape((len(lons), len(lats), len(altProfile))))
