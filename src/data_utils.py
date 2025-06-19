"""
Utility helpers for the 360-DNM toy repo.
Run ensure_example_data("data") once to drop two minimal example
files into <repo>/data/ so notebooks work even offline.
"""

from pathlib import Path
import numpy as np

def _make_synthetic_eeg(path: Path, n_channels: int = 64, n_samples: int = 200):
    """Save a tiny (n_channels × n_samples) EEG array as .npy."""
    rng = np.random.default_rng(0)
    data = 1e-6 * rng.normal(size=(n_channels, n_samples))   # micro-volt level
    np.save(path, data)

def _make_synthetic_scene_graphs(path: Path, n_graphs: int = 3):
    """Save a list-like structure of n tiny ‘scene graphs’ as .npz."""
    rng = np.random.default_rng(0)
    graphs = [rng.integers(0, 10, size=(6, 6)) for _ in range(n_graphs)]
    np.savez_compressed(path, *graphs)

def ensure_example_data(folder: str | Path = "data"):
    """
    Create minimal example datasets if they do not already exist.
    `folder` is created if necessary.
    """
    folder = Path(folder)
    folder.mkdir(exist_ok=True)

    eeg_file  = folder / "synthetic_EEG.npy"
    graph_file = folder / "synthetic_scene_graphs.npz"

    if not eeg_file.exists():
        _make_synthetic_eeg(eeg_file)
        print(f"Wrote {eeg_file.name}")

    if not graph_file.exists():
        _make_synthetic_scene_graphs(graph_file)
        print(f"Wrote {graph_file.name}")

    if eeg_file.exists() and graph_file.exists():
        print("✓  Example data ready.")
