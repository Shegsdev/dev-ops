import os
import platform
import subprocess
import re
import socket

def ping_google():
    host = "google.com"
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        if "unreachable" in output.lower():
            print("Google is unreachable.")
        else:
            print("Google is reachable.")
    except subprocess.CalledProcessError:
        print("Failed to ping Google.")

def get_google_uptime():
    try:
        domain = "google.com"
        command = ["whois", domain]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        uptime_match = re.search(r'Registered On:\s*(\d{4}-\d{2}-\d{2})', output)
        if uptime_match:
            print(f"Google.com was registered on: {uptime_match.group(1)}")
        else:
            print("Could not retrieve Google.com's registration date.")
    except subprocess.CalledProcessError:
        print("Failed to retrieve uptime information.")
    except FileNotFoundError:
        print("WHOIS command not found. Install whois package to retrieve uptime.")

if __name__ == "__main__":
    ping_google()
    get_google_uptime()
