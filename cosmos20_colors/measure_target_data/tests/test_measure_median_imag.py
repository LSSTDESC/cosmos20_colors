"""
"""
import pytest
import numpy as np
import os
from glob import glob
from ..measure_median_imag_vs_logsm import measure_median_imag
from ...data_loader import load_cosmos20


_THIS_DRNAME = os.path.dirname(os.path.abspath(__file__))
TESTING_DRNAME = os.path.join(_THIS_DRNAME, "testing_data")

ENV_VAR_MSG = "load_cosmos20 can only be tested if COSMOS20_DRN is in the env"


def _infer_phz_from_bn(bn):
    return float(bn[bn.find("phz_") + 4 : bn.find("_imag_cut")])


@pytest.mark.skipif(os.environ.get("COSMOS20_DRN", None) is None, reason=ENV_VAR_MSG)
def test_measure_median_imag_results_agree_with_hard_coded_tabulation():
    """Recompute <Mi | Mstar, z> and enforce agreement with previous calculation.

    The purpose of this test is to freeze the calculation of <Mi | Mstar, z>.
    If this test fails, then the results of the measure_median_imag function
    no longer agree with the results tabulated in testing_data directory.

    """
    cosmos = load_cosmos20()

    bnpat = "median_imag_target_data_*.dat"
    fnames = glob(os.path.join(TESTING_DRNAME, bnpat))
    bnames = sorted([os.path.basename(fn) for fn in fnames])

    err_msg = (
        "If this test fails, then either the COSMOS-20 dataset has changed,"
        "or the measure_median_imag function has changed behavior."
    )

    for bn in bnames:
        imag_cut = float(bn[bn.find("_imag_cut") :][10:-4])
        fn = os.path.join(TESTING_DRNAME, bn)
        testing_data = np.loadtxt(fn)

        phz = _infer_phz_from_bn(bn)
        logsm_target, imag_target = measure_median_imag(cosmos, imag_cut, phz)

        imag_target_from_disk = np.interp(
            logsm_target, testing_data[:, 0], testing_data[:, 1]
        )

        assert np.allclose(logsm_target, testing_data[:, 0], rtol=0.001), err_msg
        assert np.allclose(imag_target, imag_target_from_disk, rtol=0.1), err_msg
