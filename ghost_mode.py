from stem import Signal
from stem.control import Controller
import requests
import time
import socks
import socket
import sys

# 設定 Tor 作為全域 proxy
def get_ip():
    try:
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        return requests.get("http://icanhazip.com", proxies=proxies, timeout=10).text.strip()
    except Exception as e:
        return f"Unable to get IP: {e}"


def get_ip():
    try:
        return requests.get("http://icanhazip.com", timeout=10).text.strip()
    except:
        return "Unable to get IP"

def change_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="GhostMode123!")  # 替換成你設定的密碼
        controller.signal(Signal.NEWNYM)

def main():
    print("Tor service started. Please wait a moment for stabilization.")
    print("Make sure to configure your browser to use Tor for network access.\n")

    for i in range(10):
        change_ip()
        time.sleep(5)  # 等待 Tor 切換 IP
        ip = get_ip()
        print(f"[+] Your IP has been changed to : {ip}")
        time.sleep(3)

    print("\n" + " " * 10 + "GHOST MODE :)")

if __name__ == "__main__":
    main()
