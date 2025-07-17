# DetectWebsiteChangesAI
# Website Monitor with Telegram Notifications

Monitors a web page and sends Telegram alerts on changes.

## Setup

1. Clone or copy this repo.
2. Install dependencies:
pip install -r requirements.txt
3. (Optional) Edit `monitor.py` to monitor other URLs or adjust the check interval.
4. Run locally:
python monitor.py
## Deployment

### Replit
1. Import the project.
2. Click **Run**.
3. (Optional) Use UptimeRobot to ping the Repl web URL and keep it active.

### Render.com (Recommended)
1. Create a **Background Worker**.
2. Connect the repo.
3. Use `bash start.sh` as the start command.
4. Deploy! It will run 24/7 automatically.
