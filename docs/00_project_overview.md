# Project Overview

Tabletop imitation-learning project on a real **SO-101** leader/follower arm using
Hugging Face [LeRobot](https://github.com/huggingface/lerobot).

**Goal:** teach the arm a pick-and-place task — *"pick up the blue block and place it in
the blue bowl"* — from teleoperated human demonstrations, by training an ACT (Action
Chunking Transformer) policy, then (planned) compare it against a scripted OpenCV
color-detection baseline.

**Pipeline:** teleoperate (leader → follower) → record demonstrations with two cameras →
train ACT with LeRobot → push dataset + policy to the Hugging Face Hub → evaluate on the
physical robot.

**Status (2026-06):**
- Done: hardware bring-up, motor configuration, calibration, teleoperation, 23-episode
  dataset collection, ACT training (50k steps, pushed to the Hub).
- In progress / planned: on-robot policy evaluation, OpenCV baseline comparison,
  multicolor (red/green) extension.

**Hardware:** SO-101 follower + SO-101 leader (Feetech servos, 6 DoF); two cameras
(top phone mount + wrist 2 MP USB).

See [README.md](../README.md) for the public summary and [PROJECT_PLAN.md](../PROJECT_PLAN.md)
for the full 18-phase plan.
