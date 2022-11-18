import unittest
from datetime import datetime

import numpy as np

from src.echaim import density_profile, density_path, nmf2, nmf2_storm, hmf2, hmf1


class TestECHAIM(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestECHAIM, self).__init__(*args, **kwargs)
        self.dt = [
            datetime(1996, 8, 21, 5, 0, 0),
            datetime(2012, 2, 12, 16, 11, 0),
        ]
        self.lats = np.array([60, 44])
        self.lons = np.array([210, 220])
        self.alt_prof = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
        self.alt_path = np.array([200, 210])

    def test_density_profile(self):
        expected_output = np.array([
            [12367606066.263021, 108297932864.252319, 158962061260.812408, 73773659026.466248,
             39244380430.132393, 24244371947.660633, 16552247379.927717,
             12071804966.952993, 9210135282.446226, 7254833783.452740],
            [4889714776.171849, 94811918511.811340, 336738565496.773254, 133293965021.893005,
             64477786540.683990, 38014163185.852394, 25242375055.590450,
             18037499384.225201, 13520205967.189016, 10471259495.144081],
        ])
        output = density_profile(self.lats, self.lons, self.alt_prof, self.dt, False, True, False)
        self.assertTrue(np.isclose(output, expected_output).all())

    def test_density_path(self):
        expected_output = np.array([107249442422.739288, 140490116440.007843])
        output = density_path(self.lats, self.lons, self.alt_path, self.dt, True, False, False)
        self.assertTrue(np.isclose(output, expected_output).all())

    def test_nmf2(self):
        expected_output = np.array([199314753721.104797, 394486121405.954773])
        output = nmf2(self.lats, self.lons, self.dt)
        self.assertTrue(np.isclose(output, expected_output).all())

    def test_nmf2_storm(self):
        expected_output = np.array([197385080562.974884, 421941024363.300354])
        output = nmf2_storm(self.lats, self.lons, self.dt)
        self.assertTrue(np.isclose(output, expected_output).all())

    def test_hmf2(self):
        expected_output = np.array([249.101921, 266.691840])
        output = hmf2(self.lats, self.lons, self.dt)
        self.assertTrue(np.isclose(output, expected_output).all())

    def test_hmf1(self):
        expected_output = np.array([183.822682, 170.803828])
        output = hmf1(self.lats, self.lons, self.dt)
        self.assertTrue(np.isclose(output, expected_output).all())
