from src.dnm_generative import DNM
import numpy as np

def run_one_cycle():
    """Run a single 5-step cycle on random input and return the error vector."""
    model = DNM()
    fake_frame = np.random.randn(64)
    model.predict()
    error = model.observe(fake_frame)
    model.update()
    return error
