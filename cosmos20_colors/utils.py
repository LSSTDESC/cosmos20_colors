"""
"""
from jax import jit as jjit
from jax import numpy as jnp


C0 = 1 / 2
C1 = 35 / 96
C3 = -35 / 864
C5 = 7 / 2592
C7 = -5 / 69984


@jjit
def _tw_sigmoid(x, x0, tw_h, ymin, ymax):
    height_diff = ymax - ymin
    body = _tw_cuml_kern(x, x0, tw_h)
    return ymin + height_diff * body


@jjit
def _sigmoid(x, x0, k, ylo, yhi):
    height_diff = yhi - ylo
    return ylo + height_diff / (1 + jnp.exp(-k * (x - x0)))


@jjit
def _sig_slope(x, xtp, ytp, x0, slope_k, lo, hi):
    slope = _sigmoid(x, x0, slope_k, lo, hi)
    return ytp + slope * (x - xtp)


@jjit
def _tw_sig_slope(x, xtp, ytp, x0, tw_h, lo, hi):
    slope = _tw_sigmoid(x, x0, tw_h, lo, hi)
    return ytp + slope * (x - xtp)


@jjit
def _tw_cuml_kern(x, m, h):
    """Triweight kernel version of an err function."""
    z = (x - m) / h
    zz = z * z
    zzz = zz * z
    val = C0 + C1 * z + C3 * zzz + C5 * zzz * zz + C7 * zzz * zzz * z
    val = jnp.where(z < -3, 0, val)
    val = jnp.where(z > 3, 1, val)
    return val
