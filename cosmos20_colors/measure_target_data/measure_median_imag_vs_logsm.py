"""
"""
import numpy as np
from scipy.stats import binned_statistic
from ..target_data_models import get_logsm_completeness


LOGSM_MIN = 8
LOGSM_MAX = 11
DELTA_PHZ = 0.1


__all__ = ("measure_median_imag",)


def measure_median_imag(
    cat, imag_cut, phz, delta_phz=DELTA_PHZ, logsm_min=LOGSM_MIN, logsm_max=LOGSM_MAX
):
    """Measure median absolute i-band magnitude in a photo-z bin"""
    msk_phz = np.abs(cat["photoz"] - phz) < delta_phz
    logsm_cut = get_logsm_completeness(cat["photoz"], imag_cut)
    msk_logsm_complete = cat["lp_mass_med"] > logsm_cut
    csam = cat[msk_phz & msk_logsm_complete]

    logsm_bins_lo = np.max((logsm_min, csam["lp_mass_med"].min()))
    logsm_bins = np.arange(logsm_bins_lo, logsm_max, 0.1)
    logsm_binmids = 0.5 * (logsm_bins[:-1] + logsm_bins[1:])

    x, y = csam["lp_mass_med"], csam["lp_MI"]
    _res = binned_statistic(x, y, bins=logsm_bins, statistic="median")
    median_imag_sample = _res[0]

    return logsm_binmids, median_imag_sample
