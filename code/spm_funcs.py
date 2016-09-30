"""
This module defines functions implementing algorithms in SPM

Here you want the get_spm_globals function from the earlier
``four_dimensions_exercise``, with anything that function imports and other
definitions that the function needs.

See:
    https://bic-berkeley.github.io/psych-214-fall-2016/four_dimensions_exercise.html

In the same directory as this file, you will find a 'tests' directory.

Test this module with:

    python3 code/tests/test_spm_funcs.py

or better, in IPython::

    %run code/tests/test_spm_funcs.py
"""
# Python 2 compatibility
from __future__ import print_function, division

# Any imports you need
import numpy as np
import nibabel as nib


def spm_global(vol):
    """ Calculate SPM global metric for array `vol`
    SPM global metric:
        1. find mean of vol
        2. keep only voxels > mean/8
        3. return mean of remaining voxels

    Parameters
    ----------
    vol : array
        Array giving image data, usually 3D.

    Returns
    -------
    g : float
        SPM global metric for `vol`
    """
    vol_mean = np.mean(vol, axis = (0,1,2)) #scalar
    vol_subset = vol[vol>vol_mean/8] #vector
    return np.mean(vol_subset)


def get_spm_globals(fname):
    """ Calculate SPM global metrics for volumes in image filename `fname`

    Parameters
    ----------
    fname : str
        Filename of file containing 4D image

    Returns
    -------
    spm_vals : array
        SPM global metric for each 3D volume in the 4D image.
    """
    img = nib.load(fname,mmap=False)
    data = img.get_data()
    n_vols = data.shape[-1]
    spm_vals = []
    for i in range(n_vols):
        spm_vals.append(spm_global(data[...,i]))
    return spm_vals
