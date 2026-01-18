import time
import csv
import datetime
import requests

from stem.control import Controller
from stem import Signal


def run_test(
    wait_time=10,
    total_cycles=5,
    socks_port=9150,
    control_port=9151,
    log_file="log.csv"
):
    """
    Tor IP rotation test (MATLAB-callable)

    Returns
    -------
    log_file : str
        Path to CSV log file
    """

    proxies = {
        "http":  f"socks5h://127.0.0.1:{socks_port}",
        "https": f"socks5h://127.0.0.1:{socks_port}",
    }

    def get_ip():
        try:
            r = requests.get(
                "https://api.ipify.org",
                proxies=proxies,
                timeout=20
            )
            return r.text.strip()
        except Exception:
            return "ERROR"

    with open(log_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Cycle",
            "Timestamp",
            "Duration_s",
            "IP",
            "Status"
        ])

        for cycle in range(1, total_cycles + 1):
            start = time.time()
            timestamp = datetime.datetime.now().isoformat(timespec="seconds")

            try:
                with Controller.from_port(port=control_port) as c:
                    c.authenticate()
                    c.signal(Signal.NEWNYM)

                time.sleep(wait_time)

                ip = get_ip()
                status = "Success" if ip != "ERROR" else "RequestFail"

            except Exception as e:
                ip = "N/A"
                status = f"Error: {type(e).__name__}"

            duration = round(time.time() - start, 2)

            writer.writerow([
                cycle,
                timestamp,
                duration,
                ip,
                status
            ])

            print(f"[{cycle}] {status} | IP={ip}")

    return log_file


if __name__ == "__main__":
    run_test()
