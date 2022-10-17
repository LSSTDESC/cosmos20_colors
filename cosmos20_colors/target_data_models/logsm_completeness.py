"""This module implements the get_logsm_completeness function that estimates the
stellar mass completeness limit as a function of redshift and apparent i-band cut.

See notebooks/validate_logsm_completeness.ipynb

"""
import numpy as np
from collections import OrderedDict
from ..utils import _sig_slope


LOGSM_COMP_XTP = 1.0
LOGSM_COMP_K = 1.25
LOGSM_COMP_LO = 2.75
LOGSM_COMP_HI = 0.15

PARAM_DICT = OrderedDict(ytp_c0=20.305, ytp_c1=-0.465, x0_c0=-1.95, x0_c1=0.1)


__all__ = ("get_logsm_completeness",)


def get_logsm_completeness(
    redshift,
    imag_cut,
    ytp_c0=PARAM_DICT["ytp_c0"],
    ytp_c1=PARAM_DICT["ytp_c1"],
    x0_c0=PARAM_DICT["x0_c0"],
    x0_c1=PARAM_DICT["x0_c1"],
):
    """Model for Mstar completeness limit

    Parameters
    ----------
    redshift : float or ndarray of shape (n, )
        Photometric redshift derived from the Le PHARE SED-fitting code
        In the COSMOS2020_Farmer_processed_hlin.fits catalog,
        this is the `photoz` column

    imag_cut : float
        Cut in HSC measurement of i-band apparent magnitude
        In the COSMOS2020_Farmer_processed_hlin.fits catalog,
        this is the `HSC_i_MAG` column

    Returns
    -------
    logsm : float or ndarray of shape (n, )
        Cut in base-10 log of stellar mass
        In the COSMOS2020_Farmer_processed_hlin.fits catalog,
        this cut pertains to the `lp_mass_med` column

    """
    sig_slope_params = _get_sig_slope_params(imag_cut, ytp_c0, ytp_c1, x0_c0, x0_c1)
    return np.array(_sig_slope(redshift, *sig_slope_params))


def _get_sig_slope_params(imag_cut, ytp_c0, ytp_c1, x0_c0, x0_c1):
    ytp = _get_ytp(imag_cut, ytp_c0, ytp_c1)
    x0 = _get_x0(imag_cut, x0_c0, x0_c1)
    params = LOGSM_COMP_XTP, ytp, x0, LOGSM_COMP_K, LOGSM_COMP_LO, LOGSM_COMP_HI
    return params


def _get_ytp(imag_cut, ytp_c0, ytp_c1):
    return ytp_c0 + ytp_c1 * imag_cut


def _get_x0(imag_cut, x0_c0, x0_c1):
    return x0_c0 + x0_c1 * imag_cut
