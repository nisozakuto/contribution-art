#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

# Configuration
GIT_EMAIL = "nisozakuto@gmail.com"
GIT_NAME = "Niso Zakuto"
PIXEL_FILE = "pixels.txt"

# Load skip dates
HOLIDAYS_FILE = "skip_dates.txt"
if os.path.exists(HOLIDAYS_FILE):
    skip_dates = set(line.strip() for line in open(HOLIDAYS_FILE))
else:
    skip_dates = set()

today = datetime.today()
today_str = today.strftime("%Y-%m-%d")

# Skip holidays/Saturdays
if today_str not in skip_dates:
    with open(PIXEL_FILE, "a") as f:
        f.write(f"{int(today.timestamp())} pixel {today_str}\n")

    subprocess.run([
        "git", "add", PIXEL_FILE
    ], check=True)

    subprocess.run([
        "git", "commit", "-m", f"pixel {today_str}",
        "--author", f"{GIT_NAME} <{GIT_EMAIL}>",
        "--date", f"{today_str}T12:00:00"
    ], check=True)
else:
    print(f"Skipping {today_str} (holiday or Saturday)")
