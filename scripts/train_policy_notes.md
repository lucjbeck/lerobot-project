# Training Policy v1 on Google Colab

Dataset: `lucbeck/lerobot-blue-block-v1` (23 episodes, blue block → blue bowl, private)
Policy: ACT
Why Colab: MacBook Air (mps) training is slow; Colab gives a free GPU.

## Setup

1. Go to https://colab.research.google.com → New notebook
2. **Runtime → Change runtime type → GPU (T4)** → Save
3. Run the cells below in order.

## Cell 1 — confirm GPU

```python
!nvidia-smi
```

## Cell 2 — install pinned LeRobot + remove transformers

```python
!pip install -q lerobot==0.5.1
!pip uninstall -y transformers
```

IMPORTANT environment gotchas (debugged the hard way):
- Pin `lerobot==0.5.1` to match the Mac (newer PyPI releases had a broken import).
- `transformers` MUST be uninstalled. lerobot 0.5.1 treats the groot/xvla policies as
  optional and only imports them if `transformers` is present. Colab pre-installs a
  `transformers` version that crashes groot's dataclass with
  `TypeError: non-default argument 'backbone_cfg' follows default argument`.
  Removing transformers makes Colab skip groot (like the Mac) and ACT trains fine.
- After installing, **Runtime → Restart session** before continuing.

## Cell 3 — log in to Hugging Face (needed to read the private dataset)

```python
from huggingface_hub import notebook_login
notebook_login()   # call with NO arguments; paste a WRITE token into the widget
```

Never pass the token inline as an argument — it errors AND exposes the token.

## Cell 4 — mount Google Drive (so checkpoints survive disconnects)

```python
from google.colab import drive
drive.mount('/content/drive')
```

## Cell 5 — train (checkpoints to Drive every 5k steps)

```python
!lerobot-train --dataset.repo_id=lucbeck/lerobot-blue-block-v1 --policy.type=act --output_dir=/content/drive/MyDrive/lerobot/act_blue_block_v1 --job_name=act_blue_block_v1 --policy.device=cuda --steps=50000 --save_freq=5000 --wandb.enable=false --policy.repo_id=lucbeck/act-blue-block-v1 --policy.push_to_hub=true
```

Notes:
- **Steps:** ACT default is 100k. With only 23 episodes, 50k is plenty (it plateaus beforedi
  100k); 30k is fine for a faster pipeline test; below ~20k usually under-converged.
- `--save_freq=5000` writes a checkpoint to Drive every 5k steps. A disconnect costs at
  most 5k steps — resume by re-running with `--resume=true` and the same `--output_dir`.
- `--policy.push_to_hub=true` uploads the final policy to `lucbeck/act-blue-block-v1` for
  evaluation back on the Mac.
- Keep the laptop awake the whole run: plug in + run `caffeinate -dimsu` in a Terminal,
  keep the Colab tab open. Free tier disconnects on idle / caps sessions (~12h).

## After training — back on the Mac

Evaluate the policy by pointing `--policy.path` at the Hub model:

```
--policy.path=lucbeck/act-blue-block-v1
```

(full eval command comes in Phase 9 / Phase 10)

## Run log (fill in)

- Start time:
- End time:
- Final loss:
- Steps completed:
- Checkpoint pushed: lucbeck/act-blue-block-v1 (yes/no)
- Observations:
