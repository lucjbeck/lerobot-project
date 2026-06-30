# Camera Configuration

Two cameras used for v1 dataset collection:

- **Top:** phone mount, fixed overhead view of the workspace (scene localization). Kept
  stationary for the whole session.
- **Wrist:** 2 MP USB camera mounted on the arm (close-up manipulation view).

Notes:
- Verify camera indices before each session with `python scripts/check_camera.py` —
  indices can swap on reboot/replug.
- Initial single-camera testing used the MacBook built-in FaceTime camera (index 0);
  the two-camera setup above is what the v1 dataset was recorded with.
- On macOS, grant Terminal camera permission via
  System Settings → Privacy & Security → Camera.
