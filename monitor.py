import requests
import hashlib
import time

URL = "https://www.coliseodepuertorico.com/badbunnynomequieroirdeaqui/#series-buy"
CHECK_INTERVAL = 60

BOT_TOKEN = "8043404235:AAHjJFJfccWvbbj3PAjpH20-A14cb4tbPXg"
CHAT_ID = "7961394786"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print("Failed to send Telegram:", e)

def get_hash():
    try:
        response = requests.get(URL)
        return hashlib.md5(response.text.encode('utf-8')).hexdigest()
    except Exception as e:
        send_telegram(f" Error fetching URL: {e}")
        return None

def main():
    old_hash = get_hash()
    if old_hash is None:
        return
    send_telegram(f"Started monitoring: {URL}")
    while True:
        time.sleep(CHECK_INTERVAL)
        new_hash = get_hash()
        if new_hash and new_hash != old_hash:
            send_telegram(f" Page changed: {URL}")
            old_hash = new_hash

if __name__ == "__main__":
    main()
