Package Installation
====================

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


Loading the data
----------------
Once you have added installed the package and
created the COSMOS20_DRN environment variable, launch a new terminal
so that the variable is activated, and launch a python interpreter.
To load the dataset into memory:

.. code-block:: python

    >>> from cosmos20_colors import load_cosmos20
    >>> galaxies = load_cosmos20()
