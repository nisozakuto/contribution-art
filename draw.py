#!/usr/bin/env python3
import subprocess
from datetime import datetime, timedelta

# Configuration
start_date = datetime.today() - timedelta(weeks=52)
end_date = datetime.today()
skip_dates = set(line.strip() for line in open("skip_dates.txt"))

current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    
    if date_str not in skip_dates:
        # Append unique content
        with open("pixels.txt", "a") as f:
            f.write(f"{int(current_date.timestamp())} pixel {date_str}\n")
        
        # Run git commit with exact date
        subprocess.run([
            "git", "commit", "-am", f"pixel {date_str}",
            "--date", f"{date_str}T12:00:00"
        ], check=True)
    
    current_date += timedelta(days=1)
