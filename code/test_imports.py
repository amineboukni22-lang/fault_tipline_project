#!/usr/bin/env python3
"""
Test des imports essentiels
Jour 1 - Semaine Préparatoire
"""

print("=== Test des Imports ===\n")

# Imports de base
try:
    import numpy as np
    print("✓ numpy", np.__version__)
except ImportError as e:
    print("✗ numpy FAILED:", e)

try:
    import pandas as pd
    print("✓ pandas", pd.__version__)
except ImportError as e:
    print("✗ pandas FAILED:", e)

try:
    import matplotlib.pyplot as plt
    print("✓ matplotlib", plt.matplotlib.__version__)
except ImportError as e:
    print("✗ matplotlib FAILED:", e)

try:
    from scipy import stats
    import scipy
    print("✓ scipy", scipy.__version__)
except ImportError as e:
    print("✗ scipy FAILED:", e)

try:
    import plotly.graph_objects as go
    import plotly
    print("✓ plotly", plotly.__version__)
except ImportError as e:
    print("✗ plotly FAILED:", e)

# Imports avancés (peuvent échouer)
try:
    import pyvista as pv
    print("✓ pyvista", pv.__version__)
except ImportError as e:
    print("⚠ pyvista non installé (OK pour l'instant, nécessaire Mois 2)")

try:
    import h5py
    print("✓ h5py", h5py.__version__)
except ImportError as e:
    print("⚠ h5py non installé (OK pour l'instant)")

print("\n=== Test Terminé ===")
print("Si tous les packages essentiels (numpy, pandas, matplotlib, scipy, plotly)")
print("affichent ✓, vous êtes prêt à continuer !")