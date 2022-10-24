"""
"""
import numpy as np
from ..data_loader import SKY_AREA


__all__ = ("measure_cuml_imag_sky_density",)


def _cuml_counts(x, x_bins):
    cuml_counts = np.array([np.sum(x < x_cut) for x_cut in x_bins])
    return cuml_counts


def measure_cuml_imag_sky_density(cat, imag_bins):
    """Measure the cumulative density of galaxies with apparent magnitude brighter than
    the input array

    Parameters
    ----------
    cat : Astropy.table.Table
        cosmos-20 catalog

    imag_bins : ndarray of shape (n_bins, )

    Returns
    -------
    cuml_sky_density : ndarray of shape (n_bins, )
        Number counts per square degree

    """
    cuml_counts = _cuml_counts(cat["HSC_i_MAG"], imag_bins)
    cuml_sky_density = cuml_counts / SKY_AREA
    return cuml_sky_density
