# Failure Modes & Debugging

Real issues hit during setup, data collection, and training, with their fixes.
(Policy-level failure analysis is pending on-robot evaluation — Phase 10.)

## Motor configuration ([02_calibration_notes.md](02_calibration_notes.md))
- Running `lerobot-setup-motors` with all motors connected at once corrupted motor IDs
  (motors 1 and 3 dropped to the missing list). **Fix:** disconnect all motors and
  configure one at a time.
- `python -m lerobot.teleoperate` does not exist in this LeRobot version — use
  `lerobot-teleoperate`.

## Data collection ([04_dataset_collection.md](04_dataset_collection.md))
- Gripper (motor 6) tripped an Overload error when squeezing too hard or pressing into
  the table. **Fix:** gentle grip — grab and ease off.
- Follower/leader USB cables dropped when jostled mid-session. **Fix:** anchor all USB +
  power cables to the table.
- One empty episode crashed a run (`must add frames before add_episode`) from advancing
  too fast. **Fix:** don't advance until real motion is captured.
- Result: collection stopped at 23 episodes (target 50); treated as a v1 / pipeline-test
  dataset.

## Training ([../scripts/train_policy_notes.md](../scripts/train_policy_notes.md))
- Newer PyPI lerobot releases had a broken import — pinned `lerobot==0.5.1`.
- Colab's preinstalled `transformers` crashed the groot policy dataclass; uninstalling it
  makes lerobot skip groot and ACT trains fine.
