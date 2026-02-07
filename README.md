# aws-gbp-monitoring-automation
aws-gbp-monitoring-automation

# AWS GBP Monitoring Automation 🚀

This project demonstrates a cron-based Python automation system running on an AWS EC2 instance.  
It monitors GBP-related data, logs execution details, and triggers alerts when required.

---

## 🔧 Tech Stack
- AWS EC2 (Ubuntu)
- Python 3
- Cron Jobs
- Git & GitHub

---

## 📂 Project Structure
aws-automation/
├── demo.py              # Main automation script
├── email_alert.py       # Alert/notification logic
├── gbp_data.json        # Sample GBP data
├── automation.log       # Cron execution logs
├── alert.log            # Alert logs
└── README.md            # Project documentation

---

## 🔄 Architecture Flow (Diagram)

GitHub Repo
     |
     v
AWS EC2 (Ubuntu)
     |
     v
Cron Job (every 5 minutes)
     |
     v
demo.py (Python Script)
     |
     +--> automation.log
     |
     +--> email_alert.py
              |
              v
           alert.log

---

## ⚙️ How It Works
1. Code is stored and versioned on GitHub.
2. Pulled to AWS EC2 instance.
3. Cron job runs `demo.py` every 5 minutes.
4. Script processes GBP data.
5. Logs are written to `automation.log`.
6. Alerts are triggered via `email_alert.py`.

---

## ▶️ Run Manually
```bash
python3 demo.py

🕒 Cron Job Configuration
*/5 * * * * /usr/bin/python3 /home/ubuntu/aws-automation/demo.py >> /home/ubuntu/aws-automation/automation.log

👨‍💻 Author

Prem Soni
AWS / DevOps Fresher


---

## 🔥 STEP 4: Save & Exit nano
- `CTRL + O` → Enter  
- `CTRL + X`

---

## 🔥 STEP 5: Git me add karo
```bash
git status
git add README.md
git commit -m "Add professional README with architecture diagram"

