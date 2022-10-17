cosmos20_colors
===============
The cosmos20_colors package builds approximate models for the distributions of luminosity
and color of galaxies in the COSMOS-20 dataset. These approximate models are intended
to be used as rough target data for calibrating models of the galaxy--halo connection.

**Disclaimer:** Note that the cosmos20_colors package was not developed
as part of the COSMOS-20 collaboration. Please see the citation information below
if you use this package in your research.


Installation
------------
To install cosmos20_colors into your environment from the source code::

    $ cd /path/to/root/cosmos20_colors
    $ python setup.py install


Environment configuration
-------------------------
The following step is not required, but we recommend you create an environment
variable COSMOS20_DRN with the directory where the dataset is stored on your disk.
To do this, add the following line to your .bash_profile (for bash users)
or .zshrc (for zshell users)::

    export COSMOS20_DRN="/path/to/drn/containing/cosmos20/data"


Downloading the data
--------------------
The official release of the COSMOS-20 dataset is publicly available
on `the COSMOS-20 collaboration website <https://cosmos2020.calet.org/>`_.
The version of the catalog that is intended to be used with this package
can be downloaded `here <https://portal.nersc.gov/project/hacc/aphearin/cosmos20_colors/>`_.


Reading the data
----------------
Once you have downloaded the data, installed the package,
and created the COSMOS20_DRN environment variable, launch a new terminal
so that the variable is activated, and launch a python interpreter.
To load the dataset into memory:

.. code-block:: python

    >>> from cosmos20_colors import load_cosmos20
    >>> galaxies = load_cosmos20()


Testing
-------
To run the suite of unit tests::

    $ cd /path/to/root/cosmos20_colors
    $ pytest


Citation information
--------------------
If you use this package, please cite `Weaver et al. (2022) <https://arxiv.org/abs/2110.13923>`_::

    @ARTICLE{cosmos20_dataset,
           author = {{Weaver}, J.~R. and {Kauffmann}, O.~B. and {Ilbert}, O. and {McCracken}, H.~J. and {Moneti}, A. and {Toft}, S. and {Brammer}, G. and {Shuntov}, M. and {Davidzon}, I. and {Hsieh}, B.~C. and {Laigle}, C. and {Anastasiou}, A. and {Jespersen}, C.~K. and {Vinther}, J. and {Capak}, P. and {Casey}, C.~M. and {McPartland}, C.~J.~R. and {Milvang-Jensen}, B. and {Mobasher}, B. and {Sanders}, D.~B. and {Zalesky}, L. and {Arnouts}, S. and {Aussel}, H. and {Dunlop}, J.~S. and {Faisst}, A. and {Franx}, M. and {Furtak}, L.~J. and {Fynbo}, J.~P.~U. and {Gould}, K.~M.~L. and {Greve}, T.~R. and {Gwyn}, S. and {Kartaltepe}, J.~S. and {Kashino}, D. and {Koekemoer}, A.~M. and {Kokorev}, V. and {Le F{\`e}vre}, O. and {Lilly}, S. and {Masters}, D. and {Magdis}, G. and {Mehta}, V. and {Peng}, Y. and {Riechers}, D.~A. and {Salvato}, M. and {Sawicki}, M. and {Scarlata}, C. and {Scoville}, N. and {Shirley}, R. and {Silverman}, J.~D. and {Sneppen}, A. and {Smolc̆i{\'c}}, V. and {Steinhardt}, C. and {Stern}, D. and {Tanaka}, M. and {Taniguchi}, Y. and {Teplitz}, H.~I. and {Vaccari}, M. and {Wang}, W. -H. and {Zamorani}, G.},
            title = "{COSMOS2020: A Panchromatic View of the Universe to z 10 from Two Complementary Catalogs}",
          journal = {\apjs},
         keywords = {205, 1671, 594, 734, 1234, 1145, 1043, Astrophysics - Astrophysics of Galaxies, Astrophysics - Cosmology and Nongalactic Astrophysics},
             year = 2022,
            month = jan,
           volume = {258},
           number = {1},
              eid = {11},
            pages = {11},
              doi = {10.3847/1538-4365/ac3078},
    archivePrefix = {arXiv},
           eprint = {2110.13923},
     primaryClass = {astro-ph.GA},
           adsurl = {https://ui.adsabs.harvard.edu/abs/2022ApJS..258...11W},
          adsnote = {Provided by the SAO/NASA Astrophysics Data System}
    }

Please also provide the following standard acknowledgement::

    "Based on observations collected at the European Southern Observatory
    under ESO programme ID 179.A-2005 and on data products produced by CALET
    and the Cambridge Astronomy Survey Unit on behalf of the UltraVISTA consortium."
