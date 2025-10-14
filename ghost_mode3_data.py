import time
import csv
import requests
from stem import Signal
from stem.control import Controller
from datetime import datetime

# === Configurable Parameters ===
WAIT_TIME = 10             # Seconds to wait after NEWNYM (try 7 / 10 / 15)
TOTAL_CYCLES = 20          # Total number of IP rotations to test
LOG_FILE = "log.csv"       # Output CSV file

PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def get_current_ip():
    try:
        response = requests.get("http://httpbin.org/ip", proxies=PROXIES, timeout=10)
        return response.json()['origin']
    except:
        return None

def run_test():
    with open(LOG_FILE, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Cycle", "Timestamp", "Duration (s)", "IP", "Status"])

        success_count = 0
        total_duration = 0

        for i in range(1, TOTAL_CYCLES + 1):
            print(f" Cycle {i}: Requesting new IP...")

            start_time = time.time()
            renew_tor_ip()
            time.sleep(WAIT_TIME)
            ip = get_current_ip()
            duration = round(time.time() - start_time, 2)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if ip:
                status = "Success"
                success_count += 1
                total_duration += duration
                print(f"V Success: {ip} (Duration: {duration}s)")
            else:
                status = "Failed"
                print(f"X Failed (Duration: {duration}s)")

            writer.writerow([i, timestamp, duration, ip if ip else "-", status])
            time.sleep(1)

        print("\n  Test Complete!")
        print(f"Successes: {success_count}/{TOTAL_CYCLES}")
        print(f"Success Rate: {round(success_count / TOTAL_CYCLES * 100, 2)}%")
        if success_count > 0:
            print(f"Average Successful Duration: {round(total_duration / success_count, 2)} seconds")

if __name__ == "__main__":
    run_test()
