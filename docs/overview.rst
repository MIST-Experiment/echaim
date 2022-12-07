Overview
========

Description
-----------
E-CHAIM is intended as an alternative to the use of the International Reference Ionosphere (IRI) model at high
latitudes. To this end, the model represents ionospheric electron density in the region above 50°N geomagnetic latitude.
The model is composed of several sub-models, each representing a key feature in the ionospheric electron density profile.
Like the IRI, NmF2 and hmF2 are chosen as the anchor point of the profile, with all other components representing
characteristics with respect to the F2 peak density and height. Each of these sub-models feature a spherical cap
harmonic expansion in the new Altitude-Adjusted Corrected Geomagnetic (AACGM) coordinates of :cite:t:`Shepherd2014`,
calculated at 350km altitude, for the representation of the horizontal structure of the modelled parameter.
All further references to geomagnetic coordinates in this text refer to these 350km AACGM coordinates.
The order and degree of this expansion is determined experimentally, based on the amount, distribution, and quality of
available data. The seasonal variability is modelled by a Fourier expansion and solar cycle variability is modelled via
a function of solar F10.7 cm flux and IG ionospheric index.


The model papers include: :cite:t:`Themens2019`, :cite:t:`Themens2018`, :cite:t:`Themens2017`

Version
-------
The current version of the package uses `Version 3.2.4 of the C source code <https://chain-new.chain-project.net/index.php/projects/chaim/e-chaim>`_.


References
----------
.. bibliography::

