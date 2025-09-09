# Website Change Monitor

A simple Python script to monitor a given website for content changes and alert the user.

## Features

- Periodically checks a website for changes.
- Alerts the user via console output when a change is detected.
- Configurable check interval.

## Usage

1. **Install requirements**  
   This script requires Python 3 and the `requests` library.
   ```bash
   pip install requests
   ```

2. **Run the script**  
   ```bash
   python website_monitor.py <url> [interval_seconds]
   ```
   Example:
   ```bash
   python website_monitor.py https://example.com 60
   ```
   - `<url>`: The website to monitor.
   - `[interval_seconds]`: Optional. Time between checks (default: 60 seconds).

## How it works

- The script fetches the website's content and computes a hash.
- It repeatedly checks the site at the given interval.
- If the hash changes, it prints an alert to the console.

## Customization

You can extend this script to:
- Send email or desktop notifications.
- Monitor multiple sites.
- Log changes to a file.

## License

MIT License
