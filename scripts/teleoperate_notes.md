# Teleoperation

Drive the follower arm with the leader arm. Use the lerobot CLI (the
`python -m lerobot.teleoperate` form does not exist in this version).

```bash
lerobot-teleoperate \
  --robot.type=so101_follower --robot.port=$FOLLOWER_PORT --robot.id=$FOLLOWER_ID \
  --teleop.type=so101_leader  --teleop.port=$LEADER_PORT  --teleop.id=$LEADER_ID
```

Fill the variables from [../configs/environment_template.env](../configs/environment_template.env).
Requires calibration to be complete (see [../docs/02_calibration_notes.md](../docs/02_calibration_notes.md)).
Cameras are added when recording a dataset (see [record_dataset_notes.md](record_dataset_notes.md)).
