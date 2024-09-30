#!/usr/bin/env python3
import time
import subprocess
import os

def check_first():
    result = subprocess.run(['curl', 'ifconfig.me'], capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip()
        return output
    else:
        return 1

def check_second():
    result = subprocess.run(['curl', 'ipinfo.io/ip'], capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip()
        return output
    else:
        return 1

def main():
    local_time = time.localtime(time.time())
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    os.system(f'echo "\n\t{str(formatted_time)}" >> /home/kali/scripts/results_ip.txt')

    result1 = check_first()
    result2 = check_second()
    if (result1 or result2):
        if result1 != 1:
            os.system(f'echo "Result of "ifconfig.me":\t {str(result1)}" >> /home/kali/scripts/results_ip.txt')
        else:
            os.system('echo "Error with ifconfig.me" >> /home/kali/scripts/results_ip.txt')
        if result2 != 1:
            os.system(f'echo "Result of "ipinfo.io/ip":\t {str(result2)}" >> /home/kali/scripts/results_ip.txt')
        else:
            os.system('echo "Error with ipinfo.io/ip" >> /home/kali/scripts/results_ip.txt')
    else:
        os.system('echo "Global error" >> /home/kali/scripts/results_ip.txt')

    os.system('pkill firefox')
    os.system('sqlite3 /home/kali/.mozilla/firefox/r1ezo19v.default-esr/cookies.sqlite "DELETE FROM moz_cookies;"')

main() # xset dpms force off
