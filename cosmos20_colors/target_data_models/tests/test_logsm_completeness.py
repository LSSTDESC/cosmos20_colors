"""
"""
import os
import pytest
import numpy as np
from glob import glob
from ..logsm_completeness import get_logsm_completeness
from ...data_loader import load_cosmos20
from ...tests.test_data_loader import check_if_cosmos20_file_exists


HAS_COSMOS20, COSMOS20_FN, HAS_COSMOS20_MSG = check_if_cosmos20_file_exists()
IMAG_CUTS = [24, 25, 25]
PHZ_BINS = np.arange(0.4, 1.5, 0.1)

_THIS_DRNAME = os.path.dirname(os.path.abspath(__file__))
TESTING_DRNAME = os.path.join(_THIS_DRNAME, "testing_data")


@pytest.mark.parametrize("imag", IMAG_CUTS)
def test_get_logsm_completeness_evaluates(imag):
    zarr = np.linspace(0, 10, 500)
    logsm = get_logsm_completeness(zarr, imag)
    assert np.all(logsm > 0)


@pytest.mark.skipif(not HAS_COSMOS20, reason=HAS_COSMOS20_MSG)
@pytest.mark.parametrize("imag_cut", IMAG_CUTS)
def test_logsm_completeness_exceeds_reasonable_threshold(imag_cut):
    """Enforce that our Mstar completeness cut always results in at least 90% of
    galaxies at each redshift bin and for each of the imag cuts
    """

    galaxies = load_cosmos20()
    sel_hsc_i_mag = galaxies["HSC_i_MAG"] < imag_cut
    sample = galaxies[sel_hsc_i_mag]

    for phz in PHZ_BINS:
        msk_phz = np.abs(sample["photoz"] - phz) < 0.1
        logsm_cut = get_logsm_completeness(phz, imag_cut)
        n_bin = msk_phz.sum()
        msk_logsm_cut = sample["lp_mass_med"] > logsm_cut
        n_bin_complete = np.sum(msk_logsm_cut & msk_phz)
        compl_frac = n_bin_complete / n_bin
        msg = "For imag > {0} and phz~{1:.2f}, completeness frac of Mstar cut = {2:.3f}"
        assert compl_frac >= 0.9, msg.format(imag_cut, phz, compl_frac)


def test_get_logsm_completeness_is_frozen():
    """Compute the M*-completeness and enforce agreement with previous tabulation.

    The purpose of this test is to freeze the calculation of get_logsm_completeness.
    If this test fails, then the results of the get_logsm_completeness function
    no longer agree with the results tabulated in testing_data directory.

    """
    bnpat = "logsm_completeness_imag_cut_*.dat"
    fnames = glob(os.path.join(TESTING_DRNAME, bnpat))

    err_msg = (
        "If this test fails, then either the COSMOS-20 dataset has changed,"
        "or the measure_median_imag function has changed behavior."
    )
    for fn in fnames:
        bn = os.path.basename(fn)
        testing_data = np.loadtxt(fn)
        zarr, logsm_frozen = testing_data[:, 0], testing_data[:, 1]
        imag = float(bn.split("_")[-1][:-4])
        logsm_recalc = get_logsm_completeness(zarr, imag)
        assert np.allclose(logsm_frozen, logsm_recalc, atol=1e-3), err_msg
