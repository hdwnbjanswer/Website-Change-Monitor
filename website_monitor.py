import requests
import hashlib
import time
import sys

def get_website_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def calculate_hash(content):
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

def monitor_website(url, interval=60):
    print(f"Monitoring {url} for changes every {interval} seconds.")
    last_hash = None

    while True:
        content = get_website_content(url)
        if content is None:
            time.sleep(interval)
            continue

        current_hash = calculate_hash(content)
        if last_hash is None:
            last_hash = current_hash
            print("Initial content fetched and hash stored.")
        elif current_hash != last_hash:
            print(f"Website content changed at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            last_hash = current_hash
        else:
            print(f"No change detected at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(interval)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python website_monitor.py <url> [interval_seconds]")
        sys.exit(1)
    url = sys.argv[1]
    interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    monitor_website(url, interval)
