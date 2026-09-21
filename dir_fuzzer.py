#!/usr/bin/env python 3
import requests
import sys
import argparse
import threading
from queue import Queue

def parse_args():
    parser = argparse.ArgumentParser(description="Mini Directory Fuzzer")
    parser.add_argument("-u", "--url", required=True, help="URL Target, contoh: http://192.168.0.0")
    parser.add_argument("-w", "--wordlist", required=True, help="Path file Wordlist, contoh:: wordlist.txt")
    parser.add_argument("-e", "--extensions", default="", help="ekstensi file (dipisahkan koma, cth: php,html,txt)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="jumlah threads(default 10)")
    return parser.parse_args()

def worker(queue, target_url, extensions):
    while not queue.empty():
        path = queue.get()

        paths_to_check = [path]
        if extensions:
            for ext in extensions.split(","):
                ext = ext.strip()
                if ext:
                    paths_to_check.append(f"{path}.{ext}")
        for p in paths_to_check:
            url = f"{target_url}/{p}"
            try:
                response = requests.get(url, timeout=3, allow_redirects=False, headers={"User-Agent": "MiniFuzzer/2.0"})
                status = response.status_code

                if status == 200:
                    print(f"[+] [200 OK] -> {url}")
                elif status == 403:
                    print(f"[!] [403 Forbidden] -> {url}")
                elif status in [301,302]:
                    redirect_to = response.headers.get("Location", "")
                    print(f"[*] [{status} Redirect] -> {url} ---> {redirect_to}")
            except requests.exceptions.RequestException:
                pass
            
            queue.task_done()
        
def main():
    args = parse_args()
    target_url = args.url.rstrip("/")

    try:
        with open(args.wordlist, "r") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] File Wordlist '{args.wordlist}' tidak ditemukan!")
        sys.exit()
    
    queue = Queue()
    for word in words:
        queue.put(word)

    print(f"[*] Memulai Fuzzing pada target: {target_url}")
    print(f"[*] Total kata di wordlist: {len(words)}")
    print(f"[*] Menggunakan Threads: {args.threads}")
    if args.extensions:
        print(f"[*] Ekstensi tambahan: {args.extensions}")
    print ("-" * 50)

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=worker, kwargs={"queue": queue, "target_url": target_url, "extensions": args.extensions})
        t.daemon = True
        t.start()
        threads.append(t)


    queue.join()
    print("-" * 50)
    print("[*] Fuzzing selesai!")
if __name__ == "__main__":
    main()