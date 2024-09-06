#!/usr/bin/env python

#Note:Run command 'sudo su' > [your password]
#Locate the script and type the command python3 mac_changer.py

import subprocess

mac = input('Enter a new MAC address :>  ')
interface = input("Enter your interface possible interface \'eth0\' or \'wlan0\':>   ")

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {mac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)
subprocess.call("ifconfig", shell=True)
