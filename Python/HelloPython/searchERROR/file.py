import subprocess
subprocess.call("brew install nmap",shell=True)
subprocess.call("brew install metasploit",shell=True)
# subprocess.call("msfdb init",shell=True)
# subprocess.call("msfconsole",shell=True)
subprocess.call("nmap -A --reason 192.168.1.0/24",shell=True)