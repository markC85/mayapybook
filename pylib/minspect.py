import sys
import pymel.core as pmc

def syspath():
    """Return the current Python sys.path as a list of strings."""
    print("sys.paths Found:")
    for p in sys.path:
        print(f"  {p}")