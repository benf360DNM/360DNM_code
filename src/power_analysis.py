# src/power_analysis.py
import numpy as np

# ---------- P1 ----------
def simulate_p1(n_subjs=24, true_latency=45, noise=8):
    """Return synthetic audiovisual fusion-window latencies (ms)."""
    return np.random.normal(true_latency, noise, n_subjs)

# ---------- P2 ----------
def simulate_p2(n_subjs=30, baseline=0.85, drop_pct=0.25):
    """Return holistic-scene accuracy before/after cTBS."""
    before = np.random.binomial(100, baseline, n_subjs) / 100
    after  = before * (1 - drop_pct)
    return before, after

# ---------- P3 ----------
def simulate_p3(n_nights=20, beta=0.45, replay_boost=0.15, noise=0.1):
    """Return dream-coherence scores at 0 % and +15 % replay speed."""
    base = np.random.normal(0.4, noise, n_nights)
    boosted = base + beta * replay_boost
    return base, boosted

# ---------- P4 ----------
def simulate_p4(n_trials=200, p3b_mu=8, eps_var=25):
    """Return P3b amplitudes and ΣΠε² novelty metric."""
    p3b = np.random.gamma(shape=2, scale=4, size=n_trials)
    eps2 = np.random.normal(30, np.sqrt(eps_var), n_trials)
    return p3b, eps2

# ---------- P5 ----------
def simulate_p5(n_subjs=18, r_true=0.55):
    rng = np.random.default_rng()
    x = rng.normal(size=n_subjs)
    y = r_true * x + np.sqrt(1 - r_true**2) * rng.normal(size=n_subjs)
    return x, y  # beta-band gain, continuity ratings

# ---------- P6 ----------
def simulate_p6(n_trials=120, r2_target=0.30):
    rng = np.random.default_rng()
    phase = rng.uniform(-np.pi, np.pi, n_trials)
    vivid  = np.sin(phase) + rng.normal(scale=np.sqrt(1/r2_target - 1), size=n_trials)
    return phase, vivid

# ---------- P7 ----------
def simulate_p7(n_subjs=25, placebo=7.5, reduction=0.30, noise=2):
    """Return P3b amplitudes for placebo vs ketamine."""
    plc = np.random.normal(placebo, noise, n_subjs)
    ket = plc * (1 - reduction)
    return plc, ket
