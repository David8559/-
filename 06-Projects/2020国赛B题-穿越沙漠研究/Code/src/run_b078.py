"""Run and export the B078 first-level baseline results."""

from __future__ import annotations

import csv
from pathlib import Path

from b078_core import (
    B078_FIRST_SPECIAL_MAP,
    B078_FIRST_WEATHER,
    solve_mining_backtracking,
    solve_no_mining,
)
from desert_core import FIRST_LEVEL_CONFIG


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "b078_first_level_strategy.csv"


def main() -> None:
    no_mining = solve_no_mining(
        FIRST_LEVEL_CONFIG,
        B078_FIRST_WEATHER,
        B078_FIRST_SPECIAL_MAP.distances[B078_FIRST_SPECIAL_MAP.start][B078_FIRST_SPECIAL_MAP.end],
    )
    mining = solve_mining_backtracking(
        FIRST_LEVEL_CONFIG,
        B078_FIRST_SPECIAL_MAP,
        B078_FIRST_WEATHER,
        refund_rate=1.0,
    )
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["day", "location", "action", "weather", "cash", "water", "food"])
        for row in mining.audit:
            writer.writerow(
                [row.day, row.location, row.action, row.weather, row.cash, row.water, row.food]
            )
    print(f"No mining: {no_mining.score:.0f} (water={no_mining.initial_water}, food={no_mining.initial_food})")
    print(
        f"Mining DFS: {mining.score:.0f} "
        f"(water={mining.initial_water}, food={mining.initial_food}, arrival day={mining.final_state.day})"
    )
    print(f"Exported audit trail: {OUTPUT}")


if __name__ == "__main__":
    main()
