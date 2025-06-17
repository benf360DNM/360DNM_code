import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
"""
Tiny sanity checks for the 360-DNM toy simulator.
Run with:  pytest   (inside dnm_env)
"""

import numpy as np
from src.dnm_generative import DNM
from src.sim_loops import run_one_cycle

def test_error_vector_is_same_shape():
    """After observe(), last_error vector should equal input shape."""
    model = DNM()
    fake_input = np.ones(64)          # length-64 vector
    model.observe(fake_input)
    assert model.last_error.shape == fake_input.shape

def test_run_one_cycle_returns_vector():
    """run_one_cycle() should return a NumPy array of length 64."""
    err = run_one_cycle()
    assert isinstance(err, np.ndarray)
    assert err.size == 64
