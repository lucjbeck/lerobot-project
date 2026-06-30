# LeRobot Color Sorter: Complete Project Plan for Claude Code

**Project owner:** Luc Beck  
**Project name:** `lerobot-color-sorter`  
**Goal:** Build, train, evaluate, and publicly document a LeRobot leader/follower arm system that sorts colored objects into bins using imitation learning, with a simple computer-vision baseline for comparison.  
**Target outcome:** A resume-grade public project with a GitHub repo, demo video, results table, project writeup, and optional Hugging Face dataset/model upload.

---

## 0. How Claude Code should use this file

Claude Code should treat this document as the master project spec.

Claude should help with:

- Creating and maintaining the project repo structure.
- Writing beginner-friendly Python scripts.
- Writing Markdown documentation.
- Helping debug command-line, Python, camera, Git, and LeRobot issues.
- Creating experiment logs, result tables, and publishing materials.
- Keeping the project organized so it becomes resume-worthy.

Claude should **not** assume everything works on the first try. Robotics projects fail constantly. The correct workflow is:

1. Make the smallest working version.
2. Document what happened.
3. Fix one issue at a time.
4. Only expand the task once the simple version works.

Whenever I ask Claude Code for help, it should first identify which phase I am in, then help me complete the next concrete checkpoint.

---

## 1. Public project summary

This project builds a tabletop robot-learning benchmark using a LeRobot-compatible leader/follower arm setup.

The final system should:

1. Use a **leader arm** to teleoperate a **follower arm**.
2. Record demonstrations of picking up colored objects and placing them into matching bins.
3. Train an imitation-learning policy using the LeRobot workflow.
4. Evaluate the trained policy on real-world trials.
5. Compare the learned policy against a simple OpenCV baseline.
6. Publish the dataset, code, writeup, and demo video.

Final public title options:

- `LeRobot Color Sorter`
- `Vision-to-Action LeRobot Sorter`
- `Imitation Learning vs Computer Vision on a Low-Cost Robot Arm`

Recommended title:

> **LeRobot Color Sorter: Imitation Learning vs Computer Vision Baseline**

---

## 2. Core technical idea

The robot sees a tabletop workspace through a fixed camera. The workspace contains one colored block at a time. The robot must pick up the block and place it into the correct color-labeled bin.

Example mapping:

| Object | Target bin |
|---|---|
| Red block | Left bin |
| Blue block | Middle bin |
| Green block | Right bin |

The project starts with one object and one bin, then expands to three colors and three bins.

---

## 3. Why this project is resume-worthy

This is not just a hardware assembly project. It demonstrates:

- Robot hardware setup.
- Leader/follower teleoperation.
- Real-world dataset collection.
- Imitation learning.
- Computer vision.
- Benchmark design.
- Evaluation methodology.
- Public technical communication.
- GitHub documentation.

Target resume bullet after completion:

> Built and open-sourced a vision-based imitation-learning system for a LeRobot robotic arm, collecting 150+ teleoperated demonstrations, training a visuomotor policy to sort colored objects, and benchmarking performance against an OpenCV scripted-control baseline across 30+ real-world trials.

Stronger resume bullet after results exist:

> Trained a low-cost LeRobot arm to autonomously sort colored objects using imitation learning, collecting 180 teleoperated demonstrations, training an ACT-based visuomotor policy, and improving full-task success from `[BASELINE_%]` to `[POLICY_%]` across `[N]` physical evaluation trials.

---

## 4. Assumptions and placeholders

This plan assumes:

- I have a LeRobot-compatible leader/follower arm setup assembled or mostly assembled.
- I have minimal software experience.
- I am probably using an SO-100 or SO-101 style arm, but the plan should be adapted to my exact robot type.
- I have a computer that can run Python and connect to the arm over USB.
- I have at least one camera: webcam, laptop camera, USB camera, phone camera, or similar.

Important placeholders Claude Code should help me fill in:

```bash
HF_USER="your_huggingface_username"
ROBOT_TYPE="so101_follower"       # or so100_follower, depending on my exact arm
TELEOP_TYPE="so101_leader"        # or so100_leader, depending on my exact leader
FOLLOWER_PORT="/dev/tty..."       # found with lerobot-find-port
LEADER_PORT="/dev/tty..."         # found with lerobot-find-port
FOLLOWER_ID="luc_follower_arm"
LEADER_ID="luc_leader_arm"
CAMERA_NAME="front"
CAMERA_INDEX="0"
PROJECT_REPO="lerobot-color-sorter"
DATASET_REPO="${HF_USER}/lerobot-color-sorter-v1"
POLICY_REPO="${HF_USER}/lerobot-color-sorter-act-v1"
```

Use the exact same `FOLLOWER_ID` and `LEADER_ID` consistently after calibration. LeRobot uses IDs to store calibration data, so changing IDs can cause confusion.

---

## 5. Safety rules

Before running robot motion:

- Keep fingers, wires, and loose objects away from the arm.
- Use a clear tabletop area.
- Be ready to unplug power if the robot moves unexpectedly.
- Start with slow, small motions.
- Do not leave the robot running unattended.
- Do not run autonomous policies near fragile objects.
- Secure the camera and bins so they do not shift.
- Stop immediately if motors overheat, buzz loudly, or fight mechanical limits.

Emergency stop options:

- Keyboard interrupt: `Ctrl+C`
- Unplug power from the arm
- Kill terminal process

Add these rules to the public README.

---

## 6. Recommended repo structure

Claude Code should create this structure:

```text
lerobot-color-sorter/
  README.md
  PROJECT_PLAN.md
  CLAUDE.md
  requirements.txt
  .gitignore

  docs/
    00_project_overview.md
    01_setup_log.md
    02_calibration_notes.md
    03_workspace_design.md
    04_dataset_collection.md
    05_training_notes.md
    06_evaluation_notes.md
    07_failure_modes.md
    08_public_writeup.md

  scripts/
    check_python.py
    check_camera.py
    find_ports_notes.md
    teleoperate_notes.md
    record_dataset_notes.md
    replay_episode_notes.md
    train_policy_notes.md
    evaluate_policy_notes.md
    cv_baseline_detector.py
    cv_baseline_controller_stub.py
    summarize_results.py

  configs/
    environment_template.env
    camera_config_notes.md
    task_config.md

  data_logs/
    demo_episode_log.csv
    evaluation_trials.csv
    failure_log.csv

  results/
    results_table.md
    success_rate_summary.csv
    plots/

  media/
    images/
    videos/
    gifs/

  publishing/
    github_readme_checklist.md
    linkedin_post_draft.md
    resume_bullets.md
    demo_video_script.md
```

---

## 7. Phase overview

| Phase | Name | Goal | Public artifact |
|---|---|---|---|
| 0 | Repo setup | Create project workspace | GitHub repo skeleton |
| 1 | Software setup | Install Python/LeRobot dependencies | Setup log |
| 2 | Hardware verification | Identify ports, motors, cameras | Calibration notes |
| 3 | Leader/follower teleoperation | Move follower with leader | First control video |
| 4 | Workspace benchmark | Build repeatable tabletop task | Workspace photo/diagram |
| 5 | Manual task success | Complete pick-and-place by teleop | Short demo clip |
| 6 | Dataset v1 | Record red-block demonstrations | Dataset log |
| 7 | Replay | Replay recorded episodes | Replay validation notes |
| 8 | Train policy v1 | Train imitation-learning model | Training notes/checkpoint |
| 9 | Evaluate policy v1 | Run autonomous trials | Results table |
| 10 | OpenCV baseline | Build simple color detector baseline | Baseline results |
| 11 | Dataset v2 | Record multicolor sorting demos | Improved dataset |
| 12 | Train/evaluate v2 | Improve success rate | Final benchmark |
| 13 | Publish | GitHub, video, writeup, resume bullet | Public project |

---

# PHASE 0 — Create the project repo

## Goal

Create a clean project folder that will eventually become the public GitHub repo.

## Tasks

1. Create local folder:

```bash
mkdir lerobot-color-sorter
cd lerobot-color-sorter
```

2. Initialize Git:

```bash
git init
```

3. Create folders:

```bash
mkdir -p docs scripts configs data_logs results/plots media/images media/videos media/gifs publishing
```

4. Create starter files:

```bash
touch README.md PROJECT_PLAN.md CLAUDE.md requirements.txt .gitignore
```

5. Add `.gitignore`:

```gitignore
# Python
__pycache__/
*.pyc
.venv/
.env

# Data and model outputs
outputs/
checkpoints/
*.ckpt
*.pt
*.pth
*.safetensors

# Large media
*.mp4
*.mov
*.avi
*.mkv

# OS files
.DS_Store

# Logs
wandb/
*.log
```

## Definition of done

- Repo folder exists.
- Git is initialized.
- Folder structure exists.
- `README.md` has at least a one-paragraph project description.

---

# PHASE 1 — Install software

## Goal

Get Python, LeRobot, camera libraries, and GitHub/Hugging Face tools working.

## Recommended environment

Use `conda` or `miniforge` if possible.

LeRobot currently recommends Python 3.12 in its installation docs. If this changes, follow the latest official LeRobot docs.

## Commands

Create environment:

```bash
conda create -y -n lerobot python=3.12
conda activate lerobot
```

Install ffmpeg if needed:

```bash
conda install ffmpeg -c conda-forge
```

Install LeRobot from PyPI first:

```bash
pip install lerobot
pip install "lerobot[feetech]"
```

Alternative if PyPI install is not enough:

```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e ".[feetech]"
```

Install extra packages for this project:

```bash
pip install opencv-python numpy pandas matplotlib huggingface_hub
```

Check install:

```bash
lerobot-info
python --version
```

Login to Hugging Face later, when ready to upload:

```bash
huggingface-cli login
```

Optional experiment tracking:

```bash
pip install wandb
wandb login
```

## Create `requirements.txt`

Claude Code should generate:

```text
lerobot
opencv-python
numpy
pandas
matplotlib
huggingface_hub
```

Add `wandb` only if I use it.

## Definition of done

- `conda activate lerobot` works.
- `python --version` shows Python 3.12 or whatever version the latest LeRobot docs require.
- `lerobot-info` runs.
- `import cv2`, `import numpy`, and `import pandas` work in Python.

---

# PHASE 2 — Identify exact hardware and ports

## Goal

Determine the exact robot type, leader type, follower type, USB ports, and camera index.

## Tasks

### 2.1 Determine robot type

Likely values:

```bash
so101_follower
so101_leader
so100_follower
so100_leader
```

Claude should help me confirm based on my hardware, photos, motor type, or assembly guide.

### 2.2 Find USB ports

Run:

```bash
lerobot-find-port
```

Do this separately for leader and follower if needed.

Record results in `docs/01_setup_log.md`:

```markdown
## Ports

Date: YYYY-MM-DD

Follower arm port: `/dev/tty...`
Leader arm port: `/dev/tty...`
Notes:
- ...
```

On macOS, ports often look like:

```text
/dev/tty.usbmodemXXXX
```

On Linux, ports often look like:

```text
/dev/ttyACM0
/dev/ttyUSB0
```

### 2.3 Find camera index

Create `scripts/check_camera.py`:

```python
import cv2

for index in range(5):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        ret, frame = cap.read()
        print(f"Camera index {index}: opened={cap.isOpened()}, frame_read={ret}")
        cap.release()
    else:
        print(f"Camera index {index}: not available")
```

Run:

```bash
python scripts/check_camera.py
```

Record the working camera index in `docs/01_setup_log.md`.

## Definition of done

- Follower port is known.
- Leader port is known.
- Camera index/path is known.
- Robot type and teleop type are known.
- These are documented in `configs/environment_template.env`.

---

# PHASE 3 — Configure motors and calibrate arms

## Goal

Configure motor IDs and calibrate the follower and leader arms.

## Important note

Only configure motor IDs when needed. If the arm is already assembled and previously configured, do not blindly reset motor IDs unless the LeRobot docs or hardware seller instructions tell you to.

## 3.1 Configure follower motors if needed

Example command for SO-101 follower:

```bash
lerobot-setup-motors \
  --robot.type=so101_follower \
  --robot.port=${FOLLOWER_PORT}
```

## 3.2 Configure leader motors if needed

Example command:

```bash
lerobot-setup-motors \
  --robot.type=so101_leader \
  --robot.port=${LEADER_PORT}
```

If using SO-100, replace `so101_*` with `so100_*`.

## 3.3 Teleoperate once to trigger calibration

Example:

```bash
python -m lerobot.teleoperate \
  --robot.type=${ROBOT_TYPE} \
  --robot.port=${FOLLOWER_PORT} \
  --robot.id=${FOLLOWER_ID} \
  --teleop.type=${TELEOP_TYPE} \
  --teleop.port=${LEADER_PORT} \
  --teleop.id=${LEADER_ID}
```

During calibration:

- Move slowly.
- Follow prompts exactly.
- Use the same IDs every time.
- Take screenshots or notes if anything is confusing.

## Calibration notes file

Create `docs/02_calibration_notes.md`:

```markdown
# Calibration Notes

Date:
Robot type:
Teleop type:
Follower ID:
Leader ID:
Follower port:
Leader port:

## What worked

## What failed

## Fixes

## Final calibration status
```

## Definition of done

- Follower moves when leader moves.
- Gripper opens/closes.
- No joints are reversed in an obvious way.
- Calibration is documented.
- I have a short video proving leader/follower control works.

---

# PHASE 4 — Teleoperate with camera

## Goal

Run leader/follower teleoperation while viewing or recording camera input.

## Example command

Adjust camera index/path as needed:

```bash
python -m lerobot.teleoperate \
  --robot.type=${ROBOT_TYPE} \
  --robot.port=${FOLLOWER_PORT} \
  --robot.id=${FOLLOWER_ID} \
  --robot.cameras="{ front: {type: opencv, index_or_path: ${CAMERA_INDEX}, width: 640, height: 480, fps: 30}}" \
  --teleop.type=${TELEOP_TYPE} \
  --teleop.port=${LEADER_PORT} \
  --teleop.id=${LEADER_ID} \
  --display_data=true
```

If this fails, simplify:

1. Teleoperate without camera.
2. Test camera separately with OpenCV.
3. Re-add camera after both work independently.

## Definition of done

- Arm can be teleoperated.
- Camera feed is visible or at least usable by LeRobot.
- Camera angle is good enough to see object and bins.

---

# PHASE 5 — Build the physical tabletop benchmark

## Goal

Create a simple, repeatable workspace for robot learning.

## Materials

- White poster board or plain table surface.
- Painter's tape.
- 1 red block or cube.
- Later: 1 blue block and 1 green block.
- 1 bin for phase 1.
- Later: 3 bins.
- Fixed camera mount.
- Good lighting.

## Layout v1: red-only pick-and-place

```text
+--------------------------------------------------+
|                                                  |
|                   [ TARGET BIN ]                 |
|                                                  |
|                                                  |
|                                                  |
|                [ START ZONE ]                    |
|                                                  |
|                                                  |
|                   [ ROBOT ]                      |
+--------------------------------------------------+
```

## Layout v2: color sorting

```text
+--------------------------------------------------+
|                                                  |
|   [ RED BIN ]      [ BLUE BIN ]     [ GREEN BIN ]|
|                                                  |
|                                                  |
|                                                  |
|                [ START ZONE ]                    |
|                                                  |
|                                                  |
|                   [ ROBOT ]                      |
+--------------------------------------------------+
```

## Rules

- Do not move camera between dataset collection and evaluation.
- Do not move bins after dataset collection starts.
- Use tape outlines so everything returns to the same place.
- Keep lighting consistent.
- Use objects that are easy for the gripper to pick up.

## Documentation

Add photos to:

```text
media/images/workspace_v1.jpg
media/images/workspace_v2.jpg
```

Create `docs/03_workspace_design.md` with:

- Workspace photo.
- Object dimensions.
- Bin positions.
- Camera position.
- Lighting notes.
- Known limitations.

## Definition of done

- Workspace is taped down.
- Camera is fixed.
- Robot can reach start zone and bin.
- Human can teleoperate at least 5 successful pick-and-place attempts.

---

# PHASE 6 — Manual task success before ML

## Goal

Prove the task is physically possible before collecting data.

## Task v1

```text
Pick up red block from start zone and place it in target bin.
```

## Procedure

Run teleoperation. Perform 10 manual trials.

Create `data_logs/demo_episode_log.csv`:

```csv
episode,date,task,object_color,start_position,teleop_success,notes
1,YYYY-MM-DD,red_to_bin,red,left,yes,clean pickup
2,YYYY-MM-DD,red_to_bin,red,center,no,missed object
```

## Definition of done

- At least 7/10 manual teleoperated attempts succeed.
- Failures are understandable and documented.
- If fewer than 7/10 succeed, fix mechanics/workspace before moving on.

---

# PHASE 7 — Record dataset v1

## Goal

Record the first imitation-learning dataset: red block to one bin.

## Dataset v1 scope

```text
Task: Pick up the red block and place it in the bin.
Episodes: 50
Object: red block only
Start positions: 5 positions, 10 episodes each
Camera: fixed front camera
Lighting: fixed
```

## Recommended episode distribution

| Start position | Episodes |
|---|---:|
| Left | 10 |
| Center-left | 10 |
| Center | 10 |
| Center-right | 10 |
| Right | 10 |

## Example record command

Exact arguments may need adjustment based on current LeRobot version.

```bash
lerobot-record \
  --robot.type=${ROBOT_TYPE} \
  --robot.port=${FOLLOWER_PORT} \
  --robot.id=${FOLLOWER_ID} \
  --robot.cameras="{ front: {type: opencv, index_or_path: ${CAMERA_INDEX}, width: 640, height: 480, fps: 30}}" \
  --teleop.type=${TELEOP_TYPE} \
  --teleop.port=${LEADER_PORT} \
  --teleop.id=${LEADER_ID} \
  --dataset.repo_id=${HF_USER}/lerobot-red-block-v1 \
  --dataset.single_task="Pick up the red block and place it in the bin" \
  --dataset.num_episodes=50 \
  --dataset.episode_time_s=15 \
  --dataset.reset_time_s=10 \
  --display_data=true
```

If the command errors, use the latest official LeRobot docs to adjust argument names.

## Recording quality rules

Good demonstration:

- Smooth motion.
- Object clearly visible.
- Gripper actually closes around object.
- Object ends inside bin.
- No accidental table bumps.

Bad demonstration:

- Missed object.
- Dropped object halfway.
- Camera blocked by hand.
- Robot hits bin or table.
- Start state not reset.

Do not train on obviously bad demos unless intentionally studying recovery.

## Dataset notes

Create `docs/04_dataset_collection.md`:

```markdown
# Dataset Collection Notes

Dataset repo:
Date:
Task:
Number of episodes:
Episode length:
Camera:
Lighting:
Object:
Start positions:

## What went well

## What went wrong

## Episodes to potentially remove

## Next dataset changes
```

## Definition of done

- 50 episodes recorded.
- Dataset can be viewed locally or on Hugging Face.
- At least 80% of demonstrations are clean.
- Notes are updated.

---

# PHASE 8 — Replay recorded episodes

## Goal

Verify that recorded actions can be replayed on the robot.

## Example command

```bash
lerobot-replay \
  --robot.type=${ROBOT_TYPE} \
  --robot.port=${FOLLOWER_PORT} \
  --robot.id=${FOLLOWER_ID} \
  --dataset.repo_id=${HF_USER}/lerobot-red-block-v1 \
  --dataset.episode=0
```

## Why replay matters

Replay checks whether:

- Data was recorded correctly.
- Motor commands are repeatable.
- Calibration is consistent.
- The physical setup is stable.

## Definition of done

- At least one episode replays without crashing.
- Replay motion looks similar to original motion.
- Any replay issues are documented.

---

# PHASE 9 — Train imitation-learning policy v1

## Goal

Train a policy to perform red-block pick-and-place autonomously.

## Recommended starting policy

Use ACT first, because it is commonly used in LeRobot real-world imitation-learning examples.

## Training command

Use GPU if available:

```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/lerobot-red-block-v1 \
  --policy.type=act \
  --output_dir=outputs/train/act_red_block_v1 \
  --job_name=act_red_block_v1 \
  --policy.device=cuda \
  --wandb.enable=false \
  --policy.repo_id=${HF_USER}/act-red-block-v1
```

For Apple Silicon:

```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/lerobot-red-block-v1 \
  --policy.type=act \
  --output_dir=outputs/train/act_red_block_v1 \
  --job_name=act_red_block_v1 \
  --policy.device=mps \
  --wandb.enable=false \
  --policy.repo_id=${HF_USER}/act-red-block-v1
```

For CPU only:

```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/lerobot-red-block-v1 \
  --policy.type=act \
  --output_dir=outputs/train/act_red_block_v1 \
  --job_name=act_red_block_v1 \
  --policy.device=cpu \
  --wandb.enable=false \
  --policy.repo_id=${HF_USER}/act-red-block-v1
```

CPU training may be slow. If local training is painful, use Google Colab or another GPU machine.

## Training notes file

Create `docs/05_training_notes.md`:

```markdown
# Training Notes

Dataset:
Policy:
Device:
Start time:
End time:
Output dir:
Final checkpoint:
Errors:
Loss notes:

## Observations

## Next changes
```

## Definition of done

- Training starts successfully.
- A checkpoint is created.
- Final checkpoint exists in `outputs/train/.../checkpoints/last/pretrained_model` or equivalent.
- Training notes are updated.

---

# PHASE 10 — Evaluate policy v1

## Goal

Run the trained policy on the robot and measure success.

## Evaluation protocol v1

Run 20 trials:

| Start position | Trials |
|---|---:|
| Left | 4 |
| Center-left | 4 |
| Center | 4 |
| Center-right | 4 |
| Right | 4 |

## Example command

```bash
lerobot-record \
  --robot.type=${ROBOT_TYPE} \
  --robot.port=${FOLLOWER_PORT} \
  --robot.id=${FOLLOWER_ID} \
  --robot.cameras="{ front: {type: opencv, index_or_path: ${CAMERA_INDEX}, width: 640, height: 480, fps: 30}}" \
  --dataset.repo_id=${HF_USER}/eval-red-block-v1 \
  --dataset.single_task="Pick up the red block and place it in the bin" \
  --dataset.num_episodes=20 \
  --dataset.episode_time_s=15 \
  --dataset.reset_time_s=10 \
  --display_data=true \
  --policy.path=outputs/train/act_red_block_v1/checkpoints/last/pretrained_model
```

If using uploaded model:

```bash
--policy.path=${HF_USER}/act-red-block-v1
```

## Evaluation log

Create `data_logs/evaluation_trials.csv`:

```csv
trial,date,policy,object_color,start_position,pickup_success,correct_bin,full_success,failure_type,notes
1,YYYY-MM-DD,act_red_block_v1,red,left,yes,yes,yes,none,clean
2,YYYY-MM-DD,act_red_block_v1,red,center,no,no,no,missed_object,gripper closed too early
```

## Failure categories

Use standardized labels:

```text
none
missed_object
gripper_slip
object_dropped
wrong_bin
collision
camera_issue
policy_freeze
workspace_shifted
other
```

## Definition of done

- 20 autonomous trials completed.
- Each trial is logged.
- Overall success rate is calculated.
- At least one evaluation clip is saved.

---

# PHASE 11 — Build OpenCV baseline

## Goal

Create a simple classical computer-vision baseline that detects object color and uses scripted behavior.

This gives the project an engineering comparison:

```text
Hand-coded vision/control baseline vs learned imitation policy
```

## Baseline v1 behavior

1. Detect colored object in camera image.
2. Estimate rough position: left, center, or right.
3. Choose one of several pre-defined pickup poses.
4. Move to object.
5. Close gripper.
6. Move to bin.
7. Open gripper.

## Important simplification

Do not try to solve full 3D robot calibration at first. Use coarse zones.

Example image zones:

```text
+----------------------------+
|                            |
|                            |
|  LEFT    CENTER    RIGHT   |
|                            |
|                            |
+----------------------------+
```

If object center is in left third of image, use pickup pose A. If center third, pose B. If right third, pose C.

## `scripts/cv_baseline_detector.py`

Claude Code should create a script that:

- Opens camera.
- Converts frame to HSV.
- Thresholds for red, blue, or green.
- Finds largest contour.
- Draws bounding box and center.
- Prints detected color and zone.

Starter script:

```python
import cv2
import numpy as np

CAMERA_INDEX = 0

COLOR_RANGES = {
    "red1": ((0, 80, 80), (10, 255, 255)),
    "red2": ((170, 80, 80), (180, 255, 255)),
    "blue": ((90, 80, 80), (130, 255, 255)),
    "green": ((35, 60, 60), (85, 255, 255)),
}


def get_zone(x, width):
    if x < width / 3:
        return "left"
    if x < 2 * width / 3:
        return "center"
    return "right"


def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera index {CAMERA_INDEX}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width = frame.shape[:2]

        masks = {}
        red_mask_1 = cv2.inRange(hsv, np.array(COLOR_RANGES["red1"][0]), np.array(COLOR_RANGES["red1"][1]))
        red_mask_2 = cv2.inRange(hsv, np.array(COLOR_RANGES["red2"][0]), np.array(COLOR_RANGES["red2"][1]))
        masks["red"] = red_mask_1 | red_mask_2
        masks["blue"] = cv2.inRange(hsv, np.array(COLOR_RANGES["blue"][0]), np.array(COLOR_RANGES["blue"][1]))
        masks["green"] = cv2.inRange(hsv, np.array(COLOR_RANGES["green"][0]), np.array(COLOR_RANGES["green"][1]))

        best = None
        for color, mask in masks.items():
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if not contours:
                continue
            contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(contour)
            if area < 300:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cx = x + w // 2
            cy = y + h // 2
            if best is None or area > best["area"]:
                best = {"color": color, "area": area, "bbox": (x, y, w, h), "center": (cx, cy)}

        if best:
            x, y, w, h = best["bbox"]
            cx, cy = best["center"]
            zone = get_zone(cx, width)
            label = f"{best['color']} / {zone}"
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
            cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
            cv2.putText(frame, label, (x, max(20, y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            print(label)

        cv2.imshow("Color detector", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
```

## Baseline controller

Start with detector only. Do not connect it to robot motion until detection is reliable.

Then create `scripts/cv_baseline_controller_stub.py` with placeholders:

```python
"""
This is a stub for the scripted OpenCV baseline.

Goal:
1. Detect object color and rough zone.
2. Select a hard-coded pickup pose.
3. Select target bin pose based on color.
4. Execute scripted motion.

Do not run this on the robot until poses are tested carefully.
"""

PICKUP_POSES = {
    "left": "TODO",
    "center": "TODO",
    "right": "TODO",
}

BIN_POSES = {
    "red": "TODO",
    "blue": "TODO",
    "green": "TODO",
}
```

Claude Code should help write the controller only after I know how to safely send actions to the robot through the installed LeRobot API.

## Definition of done

- Detector identifies red, blue, and green objects.
- Detector prints object color and zone.
- Baseline limitations are documented.
- Optional: scripted baseline attempts 10 trials.

---

# PHASE 12 — Dataset v2: multicolor sorting

## Goal

Record a larger dataset for color sorting.

## Dataset v2 scope

```text
Task: Pick up the colored block and place it in the matching bin.
Objects: red, blue, green
Bins: red, blue, green
Episodes: 150 minimum
Distribution: 50 red, 50 blue, 50 green
Start positions: varied within taped start zone
```

## Recording plan

| Color | Episodes | Notes |
|---|---:|---|
| Red | 50 | Left bin |
| Blue | 50 | Middle bin |
| Green | 50 | Right bin |

## Task prompt

Use a consistent task description:

```text
Pick up the colored block and place it in the matching color bin.
```

If LeRobot supports language-conditioned tasks in the current setup, also experiment with task descriptions like:

```text
Pick up the red block and place it in the red bin.
Pick up the blue block and place it in the blue bin.
Pick up the green block and place it in the green bin.
```

But default to one stable task description first.

## Example command

```bash
lerobot-record \
  --robot.type=${ROBOT_TYPE} \
  --robot.port=${FOLLOWER_PORT} \
  --robot.id=${FOLLOWER_ID} \
  --robot.cameras="{ front: {type: opencv, index_or_path: ${CAMERA_INDEX}, width: 640, height: 480, fps: 30}}" \
  --teleop.type=${TELEOP_TYPE} \
  --teleop.port=${LEADER_PORT} \
  --teleop.id=${LEADER_ID} \
  --dataset.repo_id=${HF_USER}/lerobot-color-sorter-v2 \
  --dataset.single_task="Pick up the colored block and place it in the matching color bin" \
  --dataset.num_episodes=150 \
  --dataset.episode_time_s=18 \
  --dataset.reset_time_s=10 \
  --display_data=true
```

## Definition of done

- 150+ episodes recorded.
- Distribution across colors is documented.
- Bad episodes are identified.
- Dataset quality notes are written.

---

# PHASE 13 — Train and evaluate policy v2

## Goal

Train the final color-sorting imitation-learning policy and evaluate it honestly.

## Training command

```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/lerobot-color-sorter-v2 \
  --policy.type=act \
  --output_dir=outputs/train/act_color_sorter_v2 \
  --job_name=act_color_sorter_v2 \
  --policy.device=cuda \
  --wandb.enable=false \
  --policy.repo_id=${HF_USER}/act-color-sorter-v2
```

Use `mps` instead of `cuda` on Apple Silicon.

## Evaluation protocol v2

Run 30 trials minimum:

| Color | Trials |
|---|---:|
| Red | 10 |
| Blue | 10 |
| Green | 10 |

Better final benchmark:

| Color | Trials |
|---|---:|
| Red | 20 |
| Blue | 20 |
| Green | 20 |

## Metrics

Track:

- Pickup success.
- Correct bin success.
- Full task success.
- Failure type.
- Notes.

## Results summary format

Create `results/results_table.md`:

```markdown
# Results

| Method | Trials | Pickup success | Correct bin success | Full task success | Notes |
|---|---:|---:|---:|---:|---|
| OpenCV baseline | TBD | TBD | TBD | TBD | TBD |
| ACT red-only v1 | 20 | TBD | TBD | TBD | Red block only |
| ACT color-sorter v2 | 30 | TBD | TBD | TBD | Red/blue/green |
```

## Definition of done

- v2 policy trained.
- 30+ evaluation trials completed.
- Results table filled in.
- Failure modes documented.
- Final demo clip recorded.

---

# PHASE 14 — Analyze failure modes

## Goal

Turn failures into a serious engineering discussion.

Create `docs/07_failure_modes.md`:

```markdown
# Failure Modes

## Missed object
Cause:
Fix attempted:
Result:

## Gripper slip
Cause:
Fix attempted:
Result:

## Wrong bin
Cause:
Fix attempted:
Result:

## Camera issue
Cause:
Fix attempted:
Result:

## Workspace shifted
Cause:
Fix attempted:
Result:
```

## Common improvements

- Add more demos for weak start positions.
- Improve lighting.
- Use larger/easier-to-grip objects.
- Move camera higher.
- Make bins bigger.
- Add more episodes for underperforming colors.
- Reduce variation until the simpler task works.
- Increase episode length if robot needs more time.

## Definition of done

- Every failure type has examples.
- At least 3 project improvements are proposed.
- Writeup honestly explains what worked and what failed.

---

# PHASE 15 — Create demo video

## Goal

Make a clear 60–90 second video that proves the project works.

## Video structure

### 0–5 seconds: Hook

Text overlay:

```text
I trained a low-cost robot arm to sort colored objects using imitation learning.
```

Show final autonomous success.

### 5–15 seconds: Hardware setup

Show:

- Leader arm.
- Follower arm.
- Camera.
- Workspace.
- Colored blocks and bins.

### 15–30 seconds: Teleoperation and dataset

Show:

- Moving leader arm.
- Follower copying motion.
- Recording demonstrations.

Overlay:

```text
Collected 150+ teleoperated demonstrations.
```

### 30–45 seconds: Training

Show:

- Terminal command.
- Training logs.
- Dataset clips.

Overlay:

```text
Trained an ACT imitation-learning policy with LeRobot.
```

### 45–70 seconds: Autonomous evaluation

Show:

- Red trial.
- Blue trial.
- Green trial.
- One failure if useful.

Overlay:

```text
Evaluated across 30+ physical trials.
```

### 70–90 seconds: Results

Show final table:

```text
OpenCV baseline: XX% success
Imitation policy: YY% success
```

End with GitHub link.

## Definition of done

- Demo video is under 90 seconds.
- Shows real autonomous attempts.
- Does not only show cherry-picked success.
- Results table is included.

---

# PHASE 16 — Write the public README

## README structure

```markdown
# LeRobot Color Sorter

I built a low-cost robot-learning system that uses a LeRobot leader/follower arm setup to collect demonstrations and train a robot arm to sort colored objects into bins.

## Demo

[Insert GIF or video link]

## Project Summary

- Hardware: LeRobot-compatible leader/follower arm, camera, tabletop workspace
- Software: Python, LeRobot, OpenCV, PyTorch, Hugging Face Hub
- ML method: Imitation learning with ACT
- Baseline: OpenCV color detection + scripted behavior
- Result: [insert final result]

## Why I Built This

I wanted to learn real-world robotics from the ground up: hardware setup, teleoperation, data collection, model training, evaluation, and public documentation.

## System Architecture

Leader arm → teleoperation → follower arm → demonstrations → LeRobot dataset → policy training → autonomous policy → evaluation

## Hardware

- Follower arm: [exact model]
- Leader arm: [exact model]
- Camera: [exact model]
- Objects: red, blue, green blocks
- Workspace: taped tabletop benchmark

## Software

- Python
- LeRobot
- OpenCV
- NumPy/Pandas
- PyTorch
- Hugging Face Hub

## Dataset

- Dataset repo: [link]
- Number of episodes: [N]
- Episode length: [seconds]
- Task: colored object sorting

## Training

- Policy: ACT
- Dataset: [dataset]
- Device: [cuda/mps/cpu]
- Training time: [time]

## Evaluation

| Method | Trials | Pickup success | Correct bin success | Full task success |
|---|---:|---:|---:|---:|
| OpenCV baseline | [N] | [X]% | [Y]% | [Z]% |
| Imitation policy | [N] | [X]% | [Y]% | [Z]% |

## Failure Modes

- Missed object
- Gripper slip
- Wrong bin
- Camera detection issue
- Workspace shift

## What I Learned

- Real-world robot learning is mostly about data quality and repeatability.
- Simple baselines are useful for understanding task difficulty.
- Consistent lighting and camera placement matter a lot.
- Evaluation needs many trials, not one cherry-picked demo.

## Next Steps

- Add more objects.
- Add language-conditioned commands.
- Try a depth camera.
- Collect recovery demonstrations.
- Compare ACT against another policy.

## Safety

This project uses moving robot hardware. Keep hands clear, use a controlled workspace, and stop the robot immediately if motion is unsafe.
```

## Definition of done

- README explains the project to a non-expert.
- README has video/GIF.
- README has results table.
- README has setup steps.
- README has honest limitations.

---

# PHASE 17 — Publish dataset/model if ready

## Goal

Upload dataset and/or trained policy to Hugging Face.

## Dataset

If `lerobot-record` already uploaded the dataset, link it in the README.

If manual upload is needed, use Hugging Face CLI or LeRobot tooling.

## Policy upload

Example command from LeRobot docs style:

```bash
hf upload ${HF_USER}/act-color-sorter-v2 \
  outputs/train/act_color_sorter_v2/checkpoints/last/pretrained_model
```

## Public dataset/model card checklist

Include:

- Task description.
- Hardware used.
- Camera setup.
- Number of episodes.
- Known limitations.
- License.
- Link to GitHub repo.
- Link to demo video.

## Definition of done

- Dataset link exists or is intentionally not public yet.
- Model link exists or is intentionally not public yet.
- README links are correct.

---

# PHASE 18 — LinkedIn, resume, and writeup

## LinkedIn post draft

Create `publishing/linkedin_post_draft.md`:

```markdown
I built my first real-world robot learning project: a LeRobot arm that sorts colored objects into bins using imitation learning.

What I did:
- Set up a leader/follower robot arm system
- Built a repeatable tabletop benchmark
- Collected [N]+ teleoperated demonstrations
- Trained an ACT-based imitation-learning policy
- Compared it against an OpenCV baseline
- Evaluated the system across [N] real-world trials

Biggest lesson: real-world robotics is less about flashy algorithms and more about clean data, repeatable setup, and honest evaluation.

GitHub: [link]
Demo: [link]
```

## Resume bullets

Create `publishing/resume_bullets.md`:

```markdown
# Resume Bullets

## Version 1
Built and open-sourced a vision-based imitation-learning system for a LeRobot robotic arm, collecting [N]+ teleoperated demonstrations, training a visuomotor policy to sort colored objects, and benchmarking performance against an OpenCV scripted-control baseline across [N]+ real-world trials.

## Version 2
Designed a tabletop robot-learning benchmark using a low-cost LeRobot leader/follower arm setup, integrating Python, OpenCV, PyTorch, and Hugging Face LeRobot to train and evaluate autonomous colored-object sorting.

## Version 3
Collected and published a LeRobot-compatible manipulation dataset with [N]+ demonstrations and trained an ACT-based policy achieving [X]% full-task success on physical color-sorting trials.
```

## Definition of done

- GitHub repo public.
- Demo video public or shareable.
- Resume bullet finalized with real numbers.
- LinkedIn post ready.

---

# 19. Suggested 6-week timeline

## Week 1 — Setup and control

- Create repo.
- Install software.
- Identify ports.
- Calibrate leader and follower.
- Teleoperate follower with leader.
- Save first movement video.

Deliverable:

```text
Leader/follower arm working + setup documentation.
```

## Week 2 — Workspace and manual pick-and-place

- Build tabletop benchmark.
- Set camera.
- Test object and bin placement.
- Complete 10 manual trials.
- Record first clean teleop demo.

Deliverable:

```text
Robot manually completes red-block pick-and-place reliably.
```

## Week 3 — Dataset v1

- Record 50 red-block demos.
- Replay an episode.
- Document dataset quality.
- Fix bad setup issues.

Deliverable:

```text
First usable imitation-learning dataset.
```

## Week 4 — Train and evaluate v1

- Train ACT policy on red-block dataset.
- Run 20 autonomous trials.
- Log success/failure.
- Record clips.

Deliverable:

```text
First autonomous robot policy with evaluation results.
```

## Week 5 — Baseline and multicolor dataset

- Build OpenCV detector.
- Optionally attempt scripted baseline.
- Expand workspace to red/blue/green bins.
- Record 150 multicolor demos.

Deliverable:

```text
Color sorting dataset + CV baseline detector.
```

## Week 6 — Final training, evaluation, publishing

- Train color-sorter policy.
- Run 30+ evaluation trials.
- Fill results table.
- Create demo video.
- Publish GitHub repo.
- Write LinkedIn post and resume bullet.

Deliverable:

```text
Public resume-grade robotics project.
```

---

# 20. Simple task ladder

If things are too hard, use this ladder. Do not skip levels.

## Level 1

Follower arm moves with leader arm.

## Level 2

Follower opens and closes gripper correctly.

## Level 3

Robot manually picks up one object.

## Level 4

Robot manually places object into one bin.

## Level 5

Camera works during teleoperation.

## Level 6

50 demonstrations recorded.

## Level 7

One episode replays.

## Level 8

Policy trains.

## Level 9

Policy runs without crashing.

## Level 10

Policy succeeds at least once autonomously.

## Level 11

Policy success rate is measured over 20+ trials.

## Level 12

Three-color sorting works at any nonzero success rate.

## Level 13

Final results are public.

---

# 21. Troubleshooting guide

## Problem: `lerobot-find-port` does not find arm

Try:

- Check USB cable supports data, not just charging.
- Check power supply is connected.
- Try another USB port.
- Try another cable.
- Restart terminal.
- Reinstall Feetech dependency.
- On Linux, check permissions for serial devices.

## Problem: camera does not open

Try:

- Change camera index from 0 to 1, 2, 3.
- Close Zoom/FaceTime/other apps using camera.
- Test with `scripts/check_camera.py`.
- Lower resolution to 640x480.

## Problem: teleoperation moves wrong joint

Try:

- Stop immediately.
- Check motor IDs.
- Check robot type and teleop type.
- Re-check calibration.
- Compare assembly to official guide.

## Problem: gripper cannot pick up object

Try:

- Use larger object.
- Add rubber bands/friction pads to gripper if safe.
- Reduce object weight.
- Change pickup orientation.
- Use cube/block instead of smooth round object.

## Problem: training runs but policy is terrible

Try:

- Make task easier.
- Add more demonstrations.
- Remove bad demonstrations.
- Keep camera/lighting fixed.
- Reduce object position variation.
- Make episode starts more consistent.
- Train red-only before multicolor.

## Problem: policy works once but not consistently

Try:

- Run many trials and log failure type.
- Identify the most common failure.
- Collect more demos for that case.
- Keep workspace from shifting.
- Add tape marks for every object/bin position.

---

# 22. Claude Code operating instructions

When helping with this repo, Claude Code should:

1. Prefer simple, readable Python over clever code.
2. Explain commands briefly before asking me to run them.
3. Ask for command output when debugging.
4. Keep all project notes in Markdown files.
5. Keep all experimental results in CSV files.
6. Never overwrite logs without asking.
7. Use real metrics instead of vague claims.
8. Keep the repo public-facing and resume-oriented.
9. Add TODOs when hardware-specific details are unknown.
10. Help me produce artifacts that look polished on GitHub.

Claude should prioritize this order:

1. Safety.
2. Robot reliably moves.
3. Dataset quality.
4. Honest evaluation.
5. Public documentation.
6. Fancy extensions.

---

# 23. Optional extensions after final project works

Do not start these until the base project is complete.

## Extension A — Language-conditioned commands

User enters:

```text
Put the red block in the left bin.
```

Robot chooses the correct behavior.

## Extension B — Self-improving dataset loop

Workflow:

1. Run policy.
2. Save failures.
3. Add corrective demonstrations.
4. Retrain.
5. Compare v1 vs v2 vs v3.

## Extension C — More objects

Add:

- Different shapes.
- Different sizes.
- Distractor objects.
- Multiple objects at once.

## Extension D — Better vision

Add:

- Depth camera.
- AprilTags.
- Object segmentation.
- Calibration from image coordinates to robot coordinates.

## Extension E — Web dashboard

Build a small dashboard showing:

- Live camera feed.
- Last detection.
- Trial count.
- Success rate.
- Failure type distribution.

---

# 24. Source links to check during implementation

Use these as living references because LeRobot commands and docs may change.

- LeRobot GitHub: https://github.com/huggingface/lerobot
- LeRobot installation docs: https://huggingface.co/docs/lerobot/installation
- SO-101 docs: https://huggingface.co/docs/lerobot/so101
- SO-100 docs: https://huggingface.co/docs/lerobot/so100
- Imitation learning on real-world robots: https://huggingface.co/docs/lerobot/il_robots
- Getting started with real-world robots: https://huggingface.co/docs/lerobot/main/en/getting_started_real_world_robot
- Hugging Face Hub CLI: https://huggingface.co/docs/huggingface_hub/guides/cli

---

# 25. Final success definition

This project is complete when I have:

- A public GitHub repo.
- A working leader/follower LeRobot setup.
- A documented tabletop benchmark.
- At least 50 red-block demonstrations.
- Ideally 150+ multicolor demonstrations.
- At least one trained imitation-learning policy.
- At least 20 real-world autonomous evaluation trials.
- A results table.
- A short demo video.
- A polished README.
- A resume bullet with real numbers.

The project is still valid even if the robot is imperfect. The key is to show a complete engineering loop:

```text
Build → teleoperate → collect data → train → evaluate → compare → document → publish
```
