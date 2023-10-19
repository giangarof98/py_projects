import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        sock.connect((ipaddress, port))
        # sock.settimeout(None)
        print("[+] Port Opened:" + str(port))
        sock.close()
    except:
        pass

targets = input("[+] Enter targets to scan (split them by coma , ): ")
ports= int(input("[+] Enter how many ports you want to scan: "))

if ',' in targets:
    print("[*] Scanning multiple targets...")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)





