# MAC Address Changer Scripts

This repository contains two Python 3 scripts for changing the MAC address of network interfaces on Linux and Windows 10 systems.

## Scripts Overview

1. **mac_changer_linux.py**: A script to change the MAC address on Linux systems using the `ifconfig` command.
2. **mac_changer_windows.py**: A script to change the MAC address on Windows 10 systems using the `netsh` command.

## Prerequisites

- Python 3.x installed on your system.
- Administrative privileges may be required to change the MAC address.
- For Linux, ensure that the `ifconfig` command is available (you may need to install `net-tools`).
- For Windows, ensure that you have the necessary permissions to modify network settings.

## Usage

### Linux

1. Open a terminal.
2. Navigate to the directory containing the `mac_changer_linux.py` script.
3. Run the script:

   ```bash
   python3 mac_changer_linux.py
   ```

4. Follow the prompts to enter the new MAC address and the network interface (e.g., `eth0` or `wlan0`).

### Windows

1. Open Command Prompt as an administrator.
2. Navigate to the directory containing the `mac_changer_windows.py` script.
3. Run the script:

   ```bash
   python mac_changer_windows.py
   ```

4. Follow the prompts to enter the new MAC address and the network interface (e.g., `Ethernet` or `Wi-Fi`).

## Important Notes

- Changing your MAC address may violate your network's terms of service. Use this script responsibly and only on networks where you have permission.
- Not all network adapters support MAC address changes. If you encounter issues, check your adapter's documentation.
- The MAC address should be in the correct format (e.g., `XX-XX-XX-XX-XX-XX` for Windows and `XX:XX:XX:XX:XX:XX` for Linux).

## License


## Acknowledgments

- Thanks to the contributors and support of Mobile Dev Group class 44B3.
```
