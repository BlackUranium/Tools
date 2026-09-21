#!/usr/bin/env python3
import socket
import sys
import argparse
import time
import threading


parser = argparse.ArgumentParser(description="simple python port scanner")
parser.add_argument("-t", "--target", required=True, help="IP Address atau Domain target")
parser.add_argument("-p","--ports", default="1-100", help="Range Port yang mau discan, contoh 1-1000")
args = parser.parse_args()
target_host = args.target

try:
    port_range = args.ports.split("-")
    start_port = int(port_range[0])
    end_port = int(port_range[1])
except Exception:
    print("[!] Format port salah. Gunakan awal-akhir, contoh: 1-1000")
    sys.exit()

print(f"[*] memulai scanning pada target: {target_host}")
print(f"[*] target port: {start_port} sampai {end_port}")
print("-" * 40)

start_time = time.time()
lock = threading.Lock()
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_host, port))
        if result == 0:
            with lock:
                print(f"[+] Port {port} : OPEN")
        s.close()
    except Exception:
        pass

threads = []

try:
    for port in range(start_port,end_port + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

except KeyboardInterrupt:
    print("\n[!] Scanner dihentikan oleh user.")
    sys.exit()

except socket.gaierror:
    print("\n[!] Host Tidak Ditemukan / gagal resolve domain")
    sys.exit()

end_time = time.time()
print("-" * 40)
print(f"[*] Selesai dalam waktu: {end_time - start_time:.2f} detik")
        