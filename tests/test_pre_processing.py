import pytest
import numpy as np
import pyxem as pxm

from hyperspy.signals import Signal2D
from vector_matching.pre_processing import get_peaks

@pytest.fixture
def dummy_dp():
    data = np.random.rand(60, 256, 256)
    dp = pxm.signals.ElectronDiffraction2D(Signal2D(data))
    return dp


def test_get_peaks_returns_correct_type(dummy_dp):
    params = {
        'method': 'laplacian_of_gaussian',
        'get_intensity': False,
        'min_sigma': 4,
        'max_sigma': 5,
        'num_sigma': 1,
        'overlap': 0.1,
        'log_scale': True,
        'exclude_border': True
    }

    result = get_peaks(dummy_dp, **params)

    print("Result type:", type(result))
    assert isinstance(result, pxm.signals.DiffractionVectors)
