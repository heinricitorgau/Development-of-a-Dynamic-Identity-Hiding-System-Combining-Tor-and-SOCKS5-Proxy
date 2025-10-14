import requests
import time
from stem import Signal
from stem.control import Controller
from datetime import datetime
import colorama
from colorama import Fore, Style
import pyfiglet

colorama.init(autoreset=True)

def get_ip():
    urls = [
        "https://api.ipify.org",
        "https://ifconfig.me/ip",
        "https://check.torproject.org/api/ip"
    ]
    for url in urls:
        try:
            proxies = {
                'http': 'socks5h://127.0.0.1:9050',
                'https': 'socks5h://127.0.0.1:9050'
            }
            r = requests.get(url, proxies=proxies, timeout=5)
            if r.ok:
                return r.text.strip()
        except:
            continue
    return None

def change_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="GhostMode123!")  # 請填你原本設定的密碼
        controller.signal(Signal.NEWNYM)

def print_ip(ip):
    now = datetime.now().strftime("%H:%M:%S")
    if ip:
        print(Fore.GREEN + f"[{now}] IP changed to: {ip}")
    else:
        print(Fore.RED + f"[{now}] Failed to retrieve IP.")

def main():
    print(Fore.CYAN + "Tor service started. Please wait a moment for stabilization.")
    print("Make sure to configure your browser to use Tor for network access.\n")

    for i in range(10):
        change_ip()
        time.sleep(5)
        ip = get_ip()
        print_ip(ip)
        time.sleep(5)

    ascii_art = pyfiglet.figlet_format("GHOST MODE :)")
    print(Fore.MAGENTA + ascii_art)

if __name__ == "__main__":
    main()
