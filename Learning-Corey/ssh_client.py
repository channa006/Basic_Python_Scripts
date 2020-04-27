# This small python script is to check if device is reachale and to enter trhe CLI "who"

import paramiko
import time

time.sleep(1)

ip = "10.236.253.63"
host = ip
username = "e5577833"
password = "91358937"

remote = paramiko.SSHClient()

remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote.connect(ip, username=username, password=password,
               look_for_keys=False, allow_agent=False)
print("SSH Connection established to " + host)

remote1 = remote.invoke_shell()
print("Interactive session has been established")

output = remote1.recv(1000)
print(output)
remote1.send("\n")

time.sleep(4)

remote1.send("who\n")

time.sleep(4)


output = remote1.recv(5000)

print(output)

with open("onetest.txt", "w") as one:

    one.write(output)
