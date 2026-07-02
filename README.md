```
██████╗ ██╗███╗   ██╗ ██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██║████╗  ██║██╔════╝     ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║██╔██╗ ██║██║  ███╗    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║██║╚██╗██║██║   ██║    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ██║██║ ╚████║╚██████╔╝    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
```
                           

![Python](https://img.shields.io/badge/Python-3.x-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Status](https://img.shields.io/badge/Build-Stable-success)  

SwiftSweep is a **multithreaded ping sweep tool** written in Python.  
It scans a subnet (e.g., `192.168.1.0/24`) to quickly find **active hosts** using ICMP echo requests.  

PingSweep

	A lightweight Python tool that performs a multithreaded ping sweep on a subnet (e.g., 192.168.1.0/24).
	It quickly discovers active hosts by sending ICMP echo requests in parallel.

Features

	• Fast scanning using multithreading
	• Supports custom subnets (default example: 192.168.1.0/24)
	• Shows only active hosts
	• Works on Linux/macOS (-c flag) and Windows (-n flag)
	• Simple, readable Python code for learning and customization
