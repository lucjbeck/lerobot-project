# Dataset Collection Notes — v1

Dataset repo: `lucbeck/lerobot-blue-block-v1` (Hugging Face, private)
Date: 2026-06-11
Task: "Pick up the blue block and place it in the blue bowl"
Episodes: 23
Total frames: 9495 (~413 frames/episode, ~14s each @ 30fps)
Cameras: front (iPhone on tripod, fixed) + wrist (USB, on arm)
Object: blue block
Bowl: blue bowl
Start positions: varied across left → center → right of the taped start zone

## What went well

- Two-camera setup (front for localization, wrist for fine manipulation) recorded cleanly
- Resume worked after crashes — no recorded episodes lost

## What went wrong

- Recorded in batches due to hardware drops:
  - Gripper (motor 6) tripped an Overload error when squeezing too hard / pressing into surfaces
  - Follower and leader USB cables dropped when jostled mid-session
  - One empty episode crashed a run ("must add frames before add_episode") — advanced too fast
- Ended at 23 episodes (target was 50). Treating this as a v1 / pipeline-test dataset.

## Recording lessons for v2

- Anchor all USB + power cables to the table so resetting blocks can't tug them
- Gentle gripper: grab and ease off, don't crush or press into the table
- Don't advance to the next episode until real motion has been captured
- Record toward 50 episodes for a stronger policy

## Next dataset changes

- More episodes (toward 50+)
- Possibly add red/green for multicolor sorting (Phase 12)
