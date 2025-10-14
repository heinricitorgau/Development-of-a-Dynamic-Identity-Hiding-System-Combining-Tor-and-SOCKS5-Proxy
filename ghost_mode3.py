import time
import requests
import socks
import socket
from stem import Signal
from stem.control import Controller
from colorama import init, Fore
import pyfiglet

# 初始化 colorama
init()

# Tor 代理設定
PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def print_banner():
    banner = pyfiglet.figlet_format("GHOST MODE :)")
    print(Fore.MAGENTA + banner + Fore.RESET)

def get_current_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", proxies=PROXIES, timeout=15)
        return response.json()['ip']
    except Exception as e:
        return f"Failed to get IP: {e}"

def renew_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # 使用 Cookie 認證（需確保 torrc 有開啟 ControlPort 與 CookieAuthentication）
            controller.signal(Signal.NEWNYM)
            print(f"{Fore.YELLOW}[Tor] Sent NEWNYM signal{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[Tor Error] Cannot renew IP: {e}{Fore.RESET}")

def ghost_mode():
    print_banner()
    print(f"{Fore.CYAN}Tor service started. Please wait a moment for stabilization.")
    print("Make sure your torrc has ControlPort 9051 and CookieAuthentication 1")
    print("Press Ctrl+C to stop.{Fore.RESET}")

    while True:
        renew_tor_ip()
        time.sleep(5)  # 等待 Tor 換 IP 穩定
        ip = get_current_ip()
        print(f"{Fore.GREEN}[{time.strftime('%H:%M:%S')}] IP changed to: {ip}{Fore.RESET}")
        time.sleep(30)  # 每 5 秒自動換一次 IP

if __name__ == "__main__":
    ghost_mode()
