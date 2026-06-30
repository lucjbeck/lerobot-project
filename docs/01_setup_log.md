# Setup Log

## Environment

Date: 2026-06-10
OS: macOS (MacBook Air)
Python: 3.12 (via Miniforge/conda)
Conda env: `lerobot`

Install commands used:
```bash
conda create -y -n lerobot python=3.12
conda activate lerobot
conda install ffmpeg -c conda-forge
pip install lerobot "lerobot[feetech]"
pip install opencv-python numpy pandas matplotlib huggingface_hub
```

Verified working: `lerobot-info`, `import cv2`, `import numpy`, `import pandas`

## Ports

Date: 2026-06-10

Follower arm port: `/dev/tty.usbmodem5B415316401`
Leader arm port: `/dev/tty.usbmodem5B415320881`
Found using: `lerobot-find-port`

## Camera

Camera index: 0 (MacBook built-in FaceTime camera)
Confirmed with: `python scripts/check_camera.py`
Note: required granting Terminal camera permission via System Settings → Privacy & Security → Camera
