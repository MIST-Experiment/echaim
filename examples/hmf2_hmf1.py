import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

from src.echaim import hmf1, hmf2

# Defining date of observation
dt = datetime(year=2015, month=4, day=9, hour=17, minute=45)

# Defining coordinate of observation
ncoords = 100
lons = np.linspace(0, 360, ncoords)
# Constant latitude (not necessarily)
lats = np.zeros(ncoords) + 75


hmF2 = hmf2(lats, lons, dt)
hmF1 = hmf1(lats, lons, dt)

fig, axs = plt.subplots(2, 1, sharex="all")
axs[0].plot(lons, hmF2)
axs[1].plot(lons, hmF1, color='red')
axs[0].set_title(f"hmF2 at lat={lats[0]}")
axs[1].set_title(f"hmF1 at lat={lats[0]}")
axs[1].set_xlabel("Longitude [deg]")
axs[0].set_ylabel("Height [km]")
axs[1].set_ylabel("Height [km]")
plt.show()
