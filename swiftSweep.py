#!/bin/python3

#this is checking all the active host from 0-254
#python3 pingSweep 192.168.1. 
#leave the last host blank

import subprocess
import threading
import sys

network = sys.argv[1]

print(r""" ____  _             ____                           
|  _ \(_)_ __   __ _/ ___|  ___ __ _ _ __  ___ _ __ 
| |_) | | '_ \ / _` \___ \ / __/ _` | '_ \/ _ \ '__|
|  __/| | | | | (_| |___) | (_| (_| | | | |  __/ |   
|_|   |_|_| |_|\__, |____/ \___\__,_|_| |_|\___|_|   
               |___/    Fast Multithreaded Ping Sweep
""")
def ping(ip):
    try:
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"[+] {ip} is active")
    except Exception as e:
        print(f"[-] Error pinging {ip}: {e}")

# Start threads
threads = []

for host in range(1, 254):
    ip = network + str(host)
    thread = threading.Thread(target=ping, args=(ip,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Scan complete.")


