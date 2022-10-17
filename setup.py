import os
from setuptools import setup, find_packages


PACKAGENAME = "cosmos20_colors"
__version__ = None
pth = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "cosmos20_colors", "_version.py"
)
with open(pth, "r") as fp:
    exec(fp.read())


setup(
    name=PACKAGENAME,
    version=__version__,
    author="Andrew Hearin",
    author_email="ahearin@anl.gov",
    description="Package measures and models summary statistics of COSMOS-20 galaxies",
    install_requires=["numpy", "astropy", "jax"],
    packages=find_packages(),
    url="https://github.com/aphearin/cosmos20_colors",
    package_data={"cosmos20_colors": ("tests/testing_data/*.dat",)},
)
