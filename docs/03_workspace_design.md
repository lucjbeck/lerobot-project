# Workspace Design

Tabletop setup for the blue-block pick-and-place task.

- **Task:** pick up a blue block from the table and place it in a blue bowl.
- **Start zone:** a taped region on the table; the block's start position is varied across
  left → center-left → center → center-right → right to give the policy positional variety.
- **Cameras:**
  - **Top:** phone mount, fixed overhead view of the workspace (block localization).
  - **Wrist:** 2 MP USB camera mounted on the arm (close-up view for fine manipulation).
- The top camera is kept fixed for the whole session — moving it would break the learned
  visual mapping.

Facts above are drawn from the dataset-collection notes; see
[04_dataset_collection.md](04_dataset_collection.md).
