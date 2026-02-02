#!/usr/bin/env python3
import time
import subprocess
import shutil
import sys

LOG_FILE = "results_ip.txt"

""" Check if curl is installed and available """
def check_curl() -> None:
     if shutil.which("curl") is None:
          print("Error: curl is not installed or not found in PATH", file=sys.stderr)
          sys.exit(1)

""" Check the global IP due the specified service """
def check_ip(url: str) -> str | None:
    try:
        result = subprocess.run(['curl', '-s', "--max-time", "5", url], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None

""" Log the result with a timestamp """
def log_results(result1: str | None, result2: str | None):
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open(LOG_FILE, "a") as f:
          f.write(f"\n\t{formatted_time}\n")
          if result1:
               f.write(f'Result of "ifconfig.me":\t {result1}\n')
          else:
               f.write("Error with ifconfig.me\n")
          if result2:
               f.write(f'Result of "ipinfo.io/ip":\t {result2}\n')
          else:
               f.write("Error with ipinfo.io/ip\n")


def main():
    check_curl()
    result1 = check_ip("ifconfig.me")
    result2 = check_ip("ipinfo.io/ip")
    log_results(result1, result2)

if __name__ == "__main__":
      main()