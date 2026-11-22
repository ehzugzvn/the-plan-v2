"""Entry program: writes the plan text to entry.txt."""

import os

PLAN = "Day 1: enter every open make.fun bounty and agent gig board with 3 entries each. Do only escrow-paid research and coding jobs ($3-50) an agent can finish alone in hours. Work 24/7, deliver same day, reinvest winnings into entry fees and more jobs. Likely $100 -> $800 in 30 days."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)
