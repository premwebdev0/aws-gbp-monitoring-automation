import subprocess
subprocess.run(["python3", "/home/ubuntu/aws-automation/email_alert.py"])
import json
from datetime import datetime
import subprocess

with open("/home/ubuntu/aws-automation/gbp_data.json") as f:
    data = json.load(f)

rating = data["rating"]
reviews = data["reviews"]
views = data["weekly_views"]

log = f"{datetime.now()} | Rating:{rating} Reviews:{reviews} Views:{views}\n"

with open("/home/ubuntu/aws-automation/automation.log", "a") as f:
    f.write(log)

# Condition (business logic)
if rating < 4.3 or views < 1000:
    subprocess.run(["python3", "/home/ubuntu/aws-automation/email_alert.py"])

