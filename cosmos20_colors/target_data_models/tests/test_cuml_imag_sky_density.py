"""
"""
import numpy as np
import os
from ..cuml_imag_sky_density import approximate_cuml_hsc_imag_sky_density


_THIS_DRNAME = os.path.dirname(os.path.abspath(__file__))
PARENT_DRNAME = os.path.dirname(os.path.dirname(_THIS_DRNAME))
TESTING_DRNAME = os.path.join(
    PARENT_DRNAME, "measure_target_data", "tests", "testing_data"
)


def test_median_hsc_imag_model_agrees_with_data():
    """Enforce target data model for N(>m_i) agrees reasonably well with data"""
    fname = os.path.join(TESTING_DRNAME, "cuml_sky_density_hsc_appmag_i.dat")
    testing_data = np.loadtxt(fname)
    imag_bins, cuml_imag_density = testing_data[:, 0], testing_data[:, 1]
    approx_cuml_imag_density = approximate_cuml_hsc_imag_sky_density(imag_bins)
    assert np.allclose(cuml_imag_density, approx_cuml_imag_density, rtol=0.05)
