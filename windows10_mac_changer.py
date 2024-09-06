#!/usr/bin/env python


import subprocess

mac = input('Enter a new MAC address (format: XX-XX-XX-XX-XX-XX):> ')
interface = input("Enter your interface (e.g., 'Ethernet' or 'Wi-Fi'):> ")

# Disable the network interface
subprocess.call(f"netsh interface set interface \"{interface}\" admin=disabled", shell=True)

# Change the MAC address
subprocess.call(f"netsh interface set interface \"{interface}\" newmac={mac}", shell=True)

# Enable the network interface
subprocess.call(f"netsh interface set interface \"{interface}\" admin=enabled", shell=True)

# Display the current configuration
subprocess.call("getmac", shell=True)
