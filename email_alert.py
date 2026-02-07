import smtplib
from email.mime.text import MIMEText
from datetime import datetime

SENDER = "alert@example.com"
RECEIVER = "owner@example.com"

msg = MIMEText(f"""
🚨 ALERT 🚨

Business ranking issue detected.
Time: {datetime.now()}

Please take action.
""")

msg["Subject"] = "Business Alert - Ranking Down"
msg["From"] = SENDER
msg["To"] = RECEIVER

# Demo only (no real SMTP)
print("Email alert triggered")

