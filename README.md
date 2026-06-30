# SO-101 Color Sorter — ACT Imitation Learning with LeRobot

Training an [ACT](https://github.com/tonyzhaozh/act) (Action Chunking Transformer) policy to perform a real-world pick-and-place task on a low-cost **SO-101** leader/follower robot arm, using Hugging Face [LeRobot](https://github.com/huggingface/lerobot). The robot learns from teleoperated human demonstrations and is intended to be benchmarked against a scripted OpenCV color-detection baseline.

> **Status:** End-to-end pipeline complete through *training*. A 23-episode demonstration dataset was collected and an ACT policy was trained (50k steps) and pushed to the Hugging Face Hub. **Quantitative on-robot evaluation is in progress** — see [Results](#results).

## What this project is

A tabletop imitation-learning project built on a real SO-101 arm:

1. **Collect** human demonstrations by teleoperating a follower arm with a leader arm while two cameras record.
2. **Train** an ACT policy on those demonstrations with LeRobot.
3. **Evaluate** the learned policy on the physical robot and (planned) compare it to a scripted OpenCV HSV-threshold baseline.

The current task is *"pick up the blue block and place it in the blue bowl"* from varied start positions, as a v1 / pipeline-validation task. A multicolor sorting extension is planned (see [PROJECT_PLAN.md](PROJECT_PLAN.md)).

## What I did, end to end

- **Hardware bring-up & motor configuration** — assembled-arm motor IDs were set with `lerobot-setup-motors`, configuring one motor at a time after discovering that connecting all motors simultaneously corrupted the IDs. ([docs/02_calibration_notes.md](docs/02_calibration_notes.md))
- **Calibration** — calibrated leader and follower so the leader drives the follower correctly across all 6 joints.
- **Teleoperation** — drove the follower with the leader arm under live two-camera view.
- **Dataset collection** — recorded **23 episodes (~9,495 frames)** of the blue-block task across left→center→right start positions, with a top phone-mount camera (fixed overhead view) plus a 2 MP wrist-mounted USB camera (on-arm close-up). Documented the hardware failure modes hit along the way (gripper overload, USB cable drops, empty-episode crash) and the fixes. ([docs/04_dataset_collection.md](docs/04_dataset_collection.md))
- **Training** — trained an **ACT policy for 50,000 steps** and pushed the checkpoint to the Hugging Face Hub. ([docs/05_training_notes.md](docs/05_training_notes.md))
- **Evaluation (in progress)** — the evaluation harness and a scripted OpenCV baseline detector are built; on-robot trial logging is underway. ([scripts/cv_baseline_detector.py](scripts/cv_baseline_detector.py), [scripts/summarize_results.py](scripts/summarize_results.py))

## Hardware & stack

| | |
|---|---|
| **Robot** | SO-101 follower arm + SO-101 leader arm (Feetech servos, 6 DoF) |
| **Cameras** | Top: phone mount (fixed overhead scene view) + wrist: 2 MP USB camera (on-arm close-up) |
| **Policy** | ACT (Action Chunking Transformer) via LeRobot |
| **Training** | 50,000 steps; GPU (Colab) |
| **Baseline** | OpenCV HSV color thresholding + contour zoning |
| **Stack** | Python 3.12, LeRobot, PyTorch, OpenCV, NumPy/Pandas, Hugging Face Hub |

## Results

Quantitative on-robot evaluation is in progress. The ACT policy vs. OpenCV baseline comparison (pickup success, correct-bin rate, full-task success) will be reported here once trials are logged — generated directly from the trial logs via [scripts/summarize_results.py](scripts/summarize_results.py), with no hand-edited numbers.

**Demonstration dataset (v1):** 23 episodes / ~9,495 frames, blue-block pick-and-place.

## Hugging Face Hub artifacts

> ⚠️ These repos are currently **private** — make them public before sharing, or these links will 404.

- **Dataset:** https://huggingface.co/datasets/lucbeck/lerobot-blue-block-v1
- **Policy:** https://huggingface.co/lucbeck/act-blue-block-v1

## Repository layout

```
configs/        hardware/env template and task + camera notes
scripts/        OpenCV baseline detector, results summarizer, camera/port checks,
                and step-by-step command notes (teleop, record, train, eval, replay)
docs/           setup, calibration, dataset, training, evaluation, failure-mode notes
data_logs/      demonstration + evaluation trial CSVs
results/        results table and plots (populated after evaluation)
media/          images / gifs / videos (not committed; see Demo link)
PROJECT_PLAN.md full 18-phase implementation plan
```

## Reproducing the environment

```bash
conda create -y -n lerobot python=3.12 && conda activate lerobot
conda install -y ffmpeg -c conda-forge
pip install lerobot "lerobot[feetech]"
pip install -r requirements.txt
# verify hardware/cameras:
lerobot-info && python scripts/check_camera.py
```

Hardware variables (ports, IDs, camera indices) live in [configs/environment_template.env](configs/environment_template.env).

## Safety

This project drives real robot hardware. Keep hands and objects clear of the arm. Use a controlled workspace and stop the robot immediately (`Ctrl+C` or cut power) if motion is unexpected.

## Credits

Built with Hugging Face [LeRobot](https://github.com/huggingface/lerobot). ACT policy after Zhao et al., *Action Chunking with Transformers*.
