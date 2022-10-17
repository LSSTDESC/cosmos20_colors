"""
"""
from ..utils import _sig_slope


XTP_IMAG_FIT = 9.5
X0_IMAG_FIT = 9.35
K_IMAG_FIT = 1.25

__all__ = ("median_hsc_imag_model",)


def median_hsc_imag_model(logsm, z):
    """Median absolute i-band magnitude as a function of stellar mass and redshift

    Parameters
    ----------
    logsm : float or ndarray of shape (n, )
        base-10 log of stellar mass

        In the COSMOS2020_Farmer_processed_hlin.fits catalog,
        this cut pertains to the `lp_mass_med` column

    redshift : float
        Photometric redshift derived from the Le PHARE SED-fitting code

        In the COSMOS2020_Farmer_processed_hlin.fits catalog,
        this is the `photoz` column

    Returns
    -------
    imag : float or ndarray of shape (n, )
        Absolute i-band magnitude through HSC filter

        In the COSMOS2020_Farmer_processed_hlin.fits catalog,
        this cut pertains to the `lp_MI` column

    """
    params = _get_sig_slope_params(z)
    return _sig_slope(logsm, *params)


def _get_sig_slope_params(z):
    ytp = _get_ytp(z)
    lo = _get_lo_slope(z)
    hi = _get_hi_slope(z)
    params = XTP_IMAG_FIT, ytp, X0_IMAG_FIT, K_IMAG_FIT, lo, hi
    return params


def _get_ytp(z):
    return _sig_slope(z, 1, -20.5, 0.8, 1, -1.1, -0.35)


def _get_lo_slope(z):
    return _sig_slope(z, 1.1, -1.9, 1.05, 3, 0.3, 0.02)


def _get_hi_slope(z):
    return _sig_slope(z, 1.0, -1.45, 1.0, 10, 0.2, 0.0)
