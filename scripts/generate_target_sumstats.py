"""Script makes measurements of COSMOS-20 summary statistics and writes to results
to disk for use as unit-testing data."""
import os
import argparse
import subprocess
import numpy as np
from cosmos20_colors.data_loader import load_cosmos20, COSMOS20_BASENAME
from cosmos20_colors.measure_target_data import measure_median_imag
from cosmos20_colors.measure_target_data import measure_cuml_imag_sky_density
from cosmos20_colors import get_logsm_completeness

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("cosmos20_colors_repo_drn", help="Path to repository")
    parser.add_argument("imag_cut", help="Apparent magnitude in HSC i-band", type=float)
    args = parser.parse_args()
    cosmos20_colors_repo_drn = args.cosmos20_colors_repo_drn
    imag_cut = args.imag_cut

    # Store SHASUM of COSMOS-20 dataset
    cosmos20_fn = os.path.join(os.environ["COSMOS20_DRN"], COSMOS20_BASENAME)
    command = "shasum {0}".format(cosmos20_fn)
    raw_result = subprocess.check_output(command, shell=True)
    actual_shasum = raw_result.strip().split()[0].decode()
    src_drn = os.path.join(cosmos20_colors_repo_drn, "cosmos20_colors")
    testing_data_drn = os.path.join(src_drn, "tests", "testing_data")
    shasum_fnout = os.path.join(testing_data_drn, "cosmos20_shasum.dat")
    with open(shasum_fnout, "w") as fout:
        fout.write(actual_shasum)

    cat = load_cosmos20(apply_cuts=True)
    sel_hsc_i_mag = cat["HSC_i_MAG"] < imag_cut
    cosmos = cat[sel_hsc_i_mag]

    # Tabulate <Mi | Mstar, z>
    cut_phz_seq = [0.35, 0.75, 1.35, 1.95]
    testing_data_drn = os.path.join(
        src_drn, "measure_target_data", "tests", "testing_data"
    )
    outpat = "median_imag_target_data_phz_{0:.2f}_imag_cut_{1:.2f}.dat"
    for phz in cut_phz_seq:
        logsm_data, median_imag_data = measure_median_imag(cosmos, imag_cut, phz)
        outdata = np.vstack((logsm_data, median_imag_data)).T
        outname = os.path.join(testing_data_drn, outpat.format(phz, imag_cut))
        np.savetxt(outname, outdata, fmt="%.4e")

    # Tabulate stellar mass completeness limits
    testing_data_drn = os.path.join(
        src_drn, "target_data_models", "tests", "testing_data"
    )
    outpat = "logsm_completeness_imag_cut_{0:.2f}.dat"
    imag_cuts = [23, 24, 25, 26]
    zarr_out = np.linspace(0, 3, 20)
    for imag in imag_cuts:
        outbase = outpat.format(imag)
        outname = os.path.join(testing_data_drn, outbase)
        logsm_complete_out = get_logsm_completeness(zarr_out, imag)
        outdata = np.vstack((zarr_out, logsm_complete_out)).T
        np.savetxt(outname, outdata, fmt="%.4e")

    # Tabulate cumulative sky density in HSC i-band
    testing_data_drn = os.path.join(
        src_drn, "measure_target_data", "tests", "testing_data"
    )
    imag_bins = np.linspace(20, 26, 100)
    cuml_imag_density = measure_cuml_imag_sky_density(cat, imag_bins)
    outdata = np.vstack((imag_bins, cuml_imag_density)).T
    outbase = "cuml_sky_density_hsc_appmag_i.dat"
    outname = os.path.join(testing_data_drn, outbase)
    np.savetxt(outname, outdata, fmt="%.4e")
