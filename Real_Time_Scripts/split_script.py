# output = ('username channa password cisco')
# output = output.splitlines()
# # print(output)
# for item in output:
#     if ("username" in item):
#         if ("test" not in item):
#             item = item.split(" ")
#             cmd = "no username " + item[1]
#             print(cmd)


# Check if Servers are reachable

import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for n in range(1, 5):
    server_ip = "192.168.20.{0}".format(n)
    rep = os.system('ping ' + server_ip)

    if rep == 0:
        print("server is up", server_ip)
    else:
        print("server is down", server_ip)
