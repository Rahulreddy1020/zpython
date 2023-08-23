import subprocess
import os
from datetime import datetime, timedelta

def git_commit_with_date(message, date):
    # Ensuring we keep existing environment and add/overwrite our custom dates
    env = {**dict(os.environ), "GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date}

    # Make a small change to a file for the commit
    with open("dummy.txt", "a") as f:
        f.write(date + "\n")

    # Staging changes
    subprocess.run(["git", "add", "dummy.txt"])

    # Commit with a custom date
    subprocess.run(["git", "commit", "-m", message], env=env)

# Ensure you are in a Git repository.
result = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if result.stdout.strip() != "true":
    raise ValueError("This script should be run inside a git repository.")

# Starting from 1st January 2022
current_date = datetime(2022, 2, 2)
end_date = datetime(2023, 3, 3)
delta = (end_date - current_date) / 1000  # Dividing the year into 1000 parts

for _ in range(10):
    # Rounding the date to remove microseconds and then converting to ISO format
    current_date_rounded = current_date.replace(microsecond=0)
    git_commit_with_date(f"Commit for {current_date_rounded}", current_date_rounded.isoformat())
    current_date += delta
