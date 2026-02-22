#Author: Alexandre L. Martins
#02/22/2026

import subprocess
import socket
import re

dominion = "vodafone.pt"
result = subprocess.run(['traceroute', dominion], capture_output=True, text=True)
stand_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

for s in result.stdout.splitlines():
   for l in s.split(" "):
       ips_find = re.findall(stand_ip, l)
       if not(ips_find == []):
           ips = str(ips_find)
           ips = ips.replace("[", "")
           ips = ips.replace("]", "")
           ips = ips.replace("'", "")
           print(ips)
           try:
               name, alias, addressable = socket.gethostbyaddr(ips)
               print(f"IP: {ips} -> Reverse Name: {name}")
           except socket.herror:
               print(f"IP: {ips} -> Name: [No register]")
           except Exception as e:
               print(f"Error {ips}: {e}")

print(result.stdout)
print(result.stderr)
print(result.returncode)
