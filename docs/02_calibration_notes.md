# Calibration Notes

Date: 2026-06-10
Robot type: so101_follower
Teleop type: so101_leader
Follower ID: luc_follower_arm
Leader ID: luc_leader_arm
Follower port: /dev/tty.usbmodem5B415316401
Leader port: /dev/tty.usbmodem5B415320881

## Motor configuration

The arm came pre-assembled but motor IDs were not all pre-configured.
Had to run `lerobot-setup-motors` for the follower arm, connecting one motor at a time.

Final motor IDs (follower):
- shoulder_pan = 1
- shoulder_lift = 2
- elbow_flex = 3
- wrist_flex = 4
- wrist_roll = 5
- gripper = 6

## What worked

- Leader arm calibrated on first teleoperate attempt
- Follower motor IDs set successfully after connecting motors one at a time
- Teleoperation fully functional after calibration

## What failed

- Running `lerobot-setup-motors` with all motors connected simultaneously corrupted motor IDs
  (added motors 1 and 3 to the missing list). Fix: disconnect all motors, configure one at a time.
- `python -m lerobot.teleoperate` does not exist in this LeRobot version — use `lerobot-teleoperate`

## Leader calibration ranges

| Joint | Min | Pos | Max |
|---|---:|---:|---:|
| shoulder_pan | 786 | 1988 | 3507 |
| shoulder_lift | 1204 | 1489 | 3599 |
| elbow_flex | 785 | 2990 | 2993 |
| wrist_flex | 518 | 1929 | 2854 |
| gripper | 2031 | 2049 | 3304 |

Calibration file saved to:
`~/.cache/huggingface/lerobot/calibration/teleoperators/so_leader/luc_leader_arm.json`

## Final calibration status

Teleop working. Leader controls follower correctly across all joints.
