"""
"""
from collections import OrderedDict
from .utils import _tw_sig_slope
import numpy as np

PARAMS = OrderedDict(xtp=23, ytp=4.5, x0=23, tw_h=5, lo=0.55, hi=0.22)


def approximate_cuml_hsc_imag_sky_density(
    imag,
    xtp=PARAMS["xtp"],
    ytp=PARAMS["ytp"],
    x0=PARAMS["x0"],
    tw_h=PARAMS["tw_h"],
    lo=PARAMS["lo"],
    hi=PARAMS["hi"],
):
    """Density per square degree of galaxies as a function of apparent i-band magnitude

    Parameters
    ----------
    imag : float or ndarray of shape (n, )

    Returns
    -------
    Number count per square degree of galaxies brighter than
    the input apparent i-band magnitude

    """
    return np.array(_tw_sig_slope(imag, xtp, ytp, x0, tw_h, lo, hi))
