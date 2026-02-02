# Know Global IP

Simple Python script to check your global IP address using two online services and log the results with timestamps

## Features

- Checks your public IP via:
	- [ifconfig.me](https://ifconfig.me)
	- [ipinfo.io/ip](https://ipinfo.io/ip)
- Logs results with a timestamp to 'results_ip.txt'
- Can be automated with a systemd service or cron.

## Usage
```bash```
python3 know_ch_ip.py

## Optional
You can find the ready .server/.timer files to automate the script in the directory optional (the example runs every hour)

## Set optional
1) Copy files: sudo cp optional/checking_myIP.* /etc/systemd/system/
2) Edit service file and set correct path (for ExecStart=/full/path/to/know_ch_ip.py)
3) Enable timer: sudo systemctl enable --now optional/checking_myIP.timer

## Requirements
	- Python3
	- curl (installed and available in PATH)