# IPMIPWN
IPMI cipher 0 attack tool

**Requirements: ipmiutils "apt-get install ipmitool"

There are a few good tools out there (Metasploit) to help you find and identify the IPMI cipher 0 vulnerability, but because its relatively trivial to exploit I have seen nothing that helps you pwn it. While it is easy to exploit, I have found I keep having to brush up on commands and junk every time I come across it which is where my tools comes in.

My IPMIPWN tool does all the real work for you, it will attempt to exploit the cipher 0 vulnerability using a list of predefined default user accounts and setup an backdoor account with a semi-random username and random password. All successful backdoors are logged in loot.log. This tool works best on Kali, it does require you to have ipmiutils "apt-get install ipmitool" and NMAP installed. Enjoy.

USAGE: python ipmipwn.py <IP>
