import pandas as pd
from pathlib import Path

EVAL_CSV = Path(__file__).parent.parent / "data_logs" / "evaluation_trials.csv"


def summarize(csv_path: Path):
    if not csv_path.exists() or csv_path.stat().st_size == 0:
        print(f"No data yet at {csv_path}")
        return
    df = pd.read_csv(csv_path)
    print(f"Total trials: {len(df)}")
    for col in ["pickup_success", "correct_bin", "full_success"]:
        if col in df.columns:
            rate = (df[col].str.lower() == "yes").mean() * 100
            print(f"  {col}: {rate:.1f}%")
    if "failure_type" in df.columns:
        print("\nFailure breakdown:")
        print(df[df["full_success"].str.lower() != "yes"]["failure_type"].value_counts().to_string())


if __name__ == "__main__":
    summarize(EVAL_CSV)
