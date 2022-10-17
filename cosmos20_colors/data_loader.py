"""Module implements the `load_cosmos20` function"""
import os
import numpy as np
from astropy.table import Table

COSMOS20_BASENAME = "COSMOS2020_Farmer_processed_hlin.fits"


__all__ = ("load_cosmos20",)


def load_cosmos20(drn=None, bn=COSMOS20_BASENAME, apply_cuts=True):
    """Load the COSMOS-20 dataset from disk and calculate quality cuts

    Parameters
    ----------
    drn : string, optional
        Absolute path to directory containing .fits file storing COSMOS-20 dataset
        Default value is os.environ['COSMOS20_DRN'].

        For bash users, add the following line to your `.bash_profile` in order to
        configure the package to use your default dataset location:

        export COSMOS20_DRN="/drn/storing/COSMOS20"

    bn : string, optional
        Absolute path to directory containing .fits file storing COSMOS-20 dataset
        Default value is COSMOS20_BASENAME set at top of module

    apply_cuts : bool, optional
        If True, returned Table will have quality cuts imposed on the data
        Default is True

    Returns
    -------
    cat : astropy.table.Table
        Table of length ngals

    """
    if drn is None:
        drn = os.environ["COSMOS20_DRN"]
    fn = os.path.join(drn, bn)
    cat = Table.read(fn, format="fits", hdu=1)

    if apply_cuts:
        cuts = []
        sel_galaxies = np.array(cat["lp_type"] == 0).astype(bool)
        cuts.append(sel_galaxies)

        msk = np.prod(cuts, axis=0).astype(bool)
        cat = cat[msk]

    return cat
