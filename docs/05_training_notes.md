# Training Notes — Policy v1 (ACT)

The detailed, reproducible runbook lives in
[../scripts/train_policy_notes.md](../scripts/train_policy_notes.md). Summary:

- **Policy:** ACT (Action Chunking Transformer).
- **Dataset:** `lucbeck/lerobot-blue-block-v1` (23 episodes, blue block → blue bowl).
- **Compute:** Google Colab, T4 GPU (MacBook Air `mps` training was too slow).
- **Key flags:** `--steps=50000 --save_freq=5000 --policy.device=cuda --wandb.enable=false`.
- **Output:** checkpoints saved to Google Drive every 5k steps; final policy pushed to
  `lucbeck/act-blue-block-v1` (`--policy.push_to_hub=true`).
- **Step-count rationale:** ACT's default is 100k; with only 23 episodes, the loss
  plateaus well before that, so 50k was used (30k is enough for a fast pipeline test;
  below ~20k tends to under-converge).

**Environment gotchas (debugged during the run):**
- Pin `lerobot==0.5.1` to match the Mac install (newer PyPI releases had a broken import).
- Uninstall `transformers` in Colab: lerobot 0.5.1 only imports the groot/xVLA policies
  when `transformers` is present, and Colab's preinstalled version crashes groot's
  dataclass. Removing it lets ACT train cleanly. Restart the session after install.

**Run log:** final loss and exact runtime were not recorded; the policy checkpoint was
pushed to `lucbeck/act-blue-block-v1`.
