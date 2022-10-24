"""
"""
import pytest
import numpy as np
import os
from ..measure_cuml_mag_density import measure_cuml_imag_sky_density
from ...data_loader import load_cosmos20
from ...tests.test_data_loader import check_if_cosmos20_file_exists


_THIS_DRNAME = os.path.dirname(os.path.abspath(__file__))
TESTING_DRNAME = os.path.join(_THIS_DRNAME, "testing_data")

HAS_COSMOS20, COSMOS20_FN, HAS_COSMOS20_MSG = check_if_cosmos20_file_exists()


@pytest.mark.skipif(not HAS_COSMOS20, reason=HAS_COSMOS20_MSG)
def test_cuml_sky_density_hsc_imag():
    """This test measures the cumulative sky density of galaxies as a function of
    apparent magnitude in the HSC i-band and enforces exact agreement with the result
    previously tabulated by the generate_target_sumstats.py script and saved to disk.

    The purpose of the test is to freeze this measurement, and so if the measurement
    is updated in future, this test will also need to be updated, along with the
    tabulated target data.
    """
    fname = os.path.join(TESTING_DRNAME, "cuml_sky_density_hsc_appmag_i.dat")
    testing_data = np.loadtxt(fname)
    imag_bins, cuml_imag_density = testing_data[:, 0], testing_data[:, 1]
    galaxies = load_cosmos20()

    remeasured_sky_density = measure_cuml_imag_sky_density(galaxies, imag_bins)

    assert np.allclose(remeasured_sky_density, cuml_imag_density, rtol=0.01)
