"""
"""
from glob import glob
import os
import pytest
import numpy as np
from ..median_imag_model import median_hsc_imag_model
from ...measure_target_data.tests import test_measure_median_imag


_THIS_DRNAME = os.path.dirname(os.path.abspath(__file__))
PARENT_DRNAME = os.path.dirname(os.path.dirname(_THIS_DRNAME))
TESTING_DRNAME = os.path.join(
    PARENT_DRNAME, "measure_target_data", "tests", "testing_data"
)


@pytest.mark.parametrize("z", (0.0, 1.0, 2.0, 10.0))
def test_median_hsc_imag_returns_array_with_expected_shape(z):
    logsm_arr = np.linspace(5, 25, 500)
    imag = median_hsc_imag_model(logsm_arr, z)
    assert imag.shape == logsm_arr.shape


def test_median_hsc_imag_model_agrees_with_data():
    """Enforce target data model for <Mi | Mstar, z> agrees reasonably well with data"""
    bnpat = "median_imag_target_data_*.dat"
    fnames = glob(os.path.join(TESTING_DRNAME, bnpat))
    bnames = sorted([os.path.basename(fn) for fn in fnames])

    for bn in bnames:
        fn = os.path.join(TESTING_DRNAME, bn)
        testing_data = np.loadtxt(fn)
        logsm_target = testing_data[:, 0]
        imag_target = testing_data[:, 1]

        phz = test_measure_median_imag._infer_phz_from_bn(bn)
        imag_pred = median_hsc_imag_model(logsm_target, phz)

        msk = logsm_target > 9

        # Enforce no errors exceed 0.3 mags for logsm>9
        assert np.allclose(imag_pred[msk], imag_target[msk], atol=0.3)

        # Enforce mean squared error is reasonably small
        diff = imag_pred - imag_target
        loss = np.sqrt(np.mean(diff[msk] * diff[msk]))
        assert loss < 0.15
