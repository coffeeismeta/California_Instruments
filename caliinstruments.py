from pyfiglet import Figlet
from colorama import Fore, Style
from scapy.all import *
import socket

f = Figlet(font='slant')
text = f.renderText('California Instruments')


lines = text.split('\n')
width = max(len(line) for line in lines)

print(Fore.GREEN + "+" + "-"*width + "+")
for line in lines:
    print(Fore.GREEN + "|" + Style.RESET_ALL + line.ljust(width) + Fore.GREEN + "|" + Style.RESET_ALL)
print(Fore.GREEN + "+" + "-" * width + "+" + Style.RESET_ALL)

print(Fore.BLUE + "For Educational Purposes Only" + Style.RESET_ALL)
print(Fore.RED + "Caution: It will take longer the wider your port range is.\n" + Style.RESET_ALL)



target_ip = input("Enter the IPv4 Address: ")
port_range = input("Enter the Port Number range (Example: 0-65535): ")
print(Fore.RED + "Caution: It will take longer the wider your port range is." + Style.RESET_ALL)

start_port, end_port = port_range.split("-")
start_port = int(start_port)
end_port = int(end_port)


def tcp_connect_scan(target, start_port, end_port):
    print(Fore.GREEN + f"[OPEN] Port {port}" + Style.RESET_ALL)
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(Fore.GREEN + f"[OPEN] {port}" + Style.RESET_ALL)
        sock.close()

tcp_connect_scan(target_ip, start_port, end_port)

