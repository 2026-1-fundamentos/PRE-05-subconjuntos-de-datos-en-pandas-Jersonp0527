"""Homework solution for pandas subset selection."""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd


def build_specific_columns(
	input_path: str | os.PathLike = "files/input/truck_event_text_partition.csv",
	output_path: str | os.PathLike = "files/output/specific-columns.csv",
) -> Path:
	"""Create the required subset of columns as a CSV file."""

	input_path = Path(input_path)
	output_path = Path(output_path)

	df = pd.read_csv(input_path)
	subset = df[["driverId", "eventType", "longitude", "latitude"]]

	output_path.parent.mkdir(parents=True, exist_ok=True)
	subset.to_csv(output_path, index=False)
	return output_path


if __name__ == "__main__":
	build_specific_columns()
