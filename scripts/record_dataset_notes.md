# Recording a Dataset

Record teleoperated demonstrations into a LeRobot dataset and push to the Hub.

```bash
lerobot-record \
  --robot.type=so101_follower --robot.port=$FOLLOWER_PORT --robot.id=$FOLLOWER_ID \
  --teleop.type=so101_leader  --teleop.port=$LEADER_PORT  --teleop.id=$LEADER_ID \
  --dataset.repo_id=$HF_USER/lerobot-blue-block-v1 \
  --dataset.single_task="Pick up the blue block and place it in the blue bowl" \
  --dataset.num_episodes=50 --dataset.episode_time_s=15 --dataset.reset_time_s=10
```

Cameras (top phone-mount + wrist 2 MP USB) are configured in the robot config; verify
indices first with [check_camera.py](check_camera.py).

**v1 run:** collection stopped at 23 episodes (target 50), ~14 s each, ~9,495 frames total.
See [../docs/04_dataset_collection.md](../docs/04_dataset_collection.md) for what went wrong
and the lessons for v2.
