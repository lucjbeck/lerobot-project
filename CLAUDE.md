# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A tabletop imitation-learning benchmark: a LeRobot leader/follower arm sorts colored blocks into matching bins. The trained policy is compared against a scripted OpenCV baseline. See [PROJECT_PLAN.md](PROJECT_PLAN.md) for the full 18-phase plan and [README.md](README.md) for current status.

## Current phase

As of 2026-06 the project is through **training**: hardware setup, calibration, teleoperation, a 23-episode dataset, and a 50k-step ACT policy are done and pushed to the Hugging Face Hub. On-robot evaluation and the OpenCV baseline are the next phases. Always confirm the current phase in README.md before suggesting next steps.

## Environment setup

```bash
conda create -y -n lerobot python=3.12
conda activate lerobot
conda install ffmpeg -c conda-forge
pip install lerobot "lerobot[feetech]"
pip install opencv-python numpy pandas matplotlib huggingface_hub
```

Verify:

```bash
lerobot-info
python scripts/check_python.py
python scripts/check_camera.py
```

Install [requirements.txt](requirements.txt) covers the non-lerobot dependencies: `opencv-python`, `numpy`, `pandas`, `matplotlib`, `huggingface_hub`.

## Key commands

Find USB ports (run for each arm separately):

```bash
lerobot-find-port
```

Teleoperate (fill in vars from `configs/environment_template.env`):

```bash
python -m lerobot.teleoperate \
  --robot.type=${ROBOT_TYPE} --robot.port=${FOLLOWER_PORT} --robot.id=${FOLLOWER_ID} \
  --teleop.type=${TELEOP_TYPE} --teleop.port=${LEADER_PORT} --teleop.id=${LEADER_ID}
```

Record dataset:

```bash
lerobot-record --robot.type=${ROBOT_TYPE} ... --dataset.repo_id=${HF_USER}/lerobot-red-block-v1 \
  --dataset.single_task="Pick up the red block and place it in the bin" \
  --dataset.num_episodes=50 --dataset.episode_time_s=15 --dataset.reset_time_s=10
```

Train (use `--policy.device=mps` on Apple Silicon, `cpu` if no GPU):

```bash
lerobot-train --dataset.repo_id=${HF_USER}/lerobot-red-block-v1 --policy.type=act \
  --output_dir=outputs/train/act_red_block_v1 --policy.device=cuda
```

Summarize evaluation results:

```bash
python scripts/summarize_results.py
```

## Architecture

```
Leader arm ──teleoperate──► Follower arm ──record──► LeRobot dataset
                                                           │
                                                     lerobot-train
                                                           │
                                                     ACT policy checkpoint
                                                           │
                                               lerobot-record --policy.path=...
                                                           │
                                                   Evaluation trials (CSV)
                                                           │
                                               scripts/summarize_results.py
```

Parallel track — OpenCV baseline:

```
Camera frame → HSV threshold → largest contour → zone (left/center/right) → scripted pickup pose
```

Key scripts:
- [scripts/cv_baseline_detector.py](scripts/cv_baseline_detector.py) — working HSV color detector with live preview
- [scripts/summarize_results.py](scripts/summarize_results.py) — reads `data_logs/evaluation_trials.csv` (created during Phase 10 evaluation), prints success rates by category and failure breakdown
- [scripts/check_camera.py](scripts/check_camera.py) — probes camera indices 0–4

Data files:
- [configs/environment_template.env](configs/environment_template.env) — all hardware variables (ports, IDs, camera indices)
- `data_logs/evaluation_trials.csv` — written during Phase 10; columns: `trial,date,policy,object_color,start_position,pickup_success,correct_bin,full_success,failure_type,notes`

## Rules

- Never overwrite existing CSV logs without asking.
- Use real numbers in results — no vague claims.
- Add `# TODO` comments when hardware-specific details are unknown.
- Keep all notes in Markdown files under [docs/](docs/).
- Keep calibration IDs (`FOLLOWER_ID=luc_follower_arm`, `LEADER_ID=luc_leader_arm`) consistent after first calibration — LeRobot stores calibration data by ID.

## Priority order

1. Safety — keep hands clear, `Ctrl+C` or unplug to stop
2. Robot reliably moves
3. Dataset quality
4. Honest evaluation
5. Public documentation
6. Extensions

## Hardware variables

All hardware variables (HF username, robot/teleop types, ports, IDs, camera indices) live in [configs/environment_template.env](configs/environment_template.env). Keep calibration IDs stable once set — LeRobot stores calibration data by ID.
