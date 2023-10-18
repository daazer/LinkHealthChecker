
import requests
import sys
import subprocess
import re
import threading
import argparse

# Global lock for thread-safe printing
print_lock = threading.Lock()

def is_url_up(url, semaphore, only_up, show_ping):
    try:
        response = requests.head(url, timeout=5)
        up = 200 <= response.status_code < 400
    except requests.RequestException:
        up = False

    domain = url.split("//")[-1].split("/")[0]
    ping_time = None
    if show_ping:
        ping_time = ping_url(domain)
    
    with print_lock:
        if up:
            if ping_time:
                print(f"{url} is up with ping time: {ping_time}ms")
            else:
                print(f"{url} is up")
        elif not only_up:
            print(f"{url} is down.")

    # Release the semaphore once the thread's task is done
    semaphore.release()

def ping_url(domain):
    try:
        if sys.platform == "win32":
            output = subprocess.check_output(["ping", "-n", "1", domain], stderr=subprocess.STDOUT, text=True)
            time = re.search(r'time=(\d+)', output).group(1)
        else:
            output = subprocess.check_output(["ping", "-c", "1", domain], stderr=subprocess.STDOUT, text=True)
            time = re.search(r'time=(\d+\.\d+)', output).group(1)
        return time
    except:
        return None

def main():
    parser = argparse.ArgumentParser(description="Check URLs for their status and ping time.")
    parser.add_argument("-L", "--list", required=True, help="File containing list of URLs to check.")
    parser.add_argument("-T", "--threads", type=int, default=10, help="Number of threads to use. Default is 10.")
    parser.add_argument("--only-up", action="store_true", help="Only display URLs that are up.")
    parser.add_argument("--show-ping", action="store_true", help="Display the ping time for URLs.")
    args = parser.parse_args()

    with open(args.list, 'r') as file:
        urls = [line.strip() for line in file]

    # Create semaphores to control the number of concurrent threads
    semaphore = threading.Semaphore(args.threads)

    # Spawn threads for each URL
    threads = []
    for url in urls:
        semaphore.acquire()
        thread = threading.Thread(target=is_url_up, args=(url, semaphore, args.only_up, args.show_ping), daemon=True)
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()