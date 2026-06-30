import sys
import importlib

print(f"Python version: {sys.version}")

packages = ["cv2", "numpy", "pandas", "matplotlib"]
for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"  {pkg}: OK")
    except ImportError:
        print(f"  {pkg}: MISSING")
