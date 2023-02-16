import subprocess


address = input('\naddress? => ')
cmd = f"ping -c 1 {address}"
subprocess.Popen(cmd, shell=True)
