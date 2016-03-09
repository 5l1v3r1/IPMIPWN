# IPMIPWN
IPMI cipher 0 attack tool

**Requirements: ipmiutils "apt-get install ipmitool"

There are a few good tools out there (Metasploit) to help you identify the IPMI cipher 0 vulnerability, but I have seen nothing that helps you exploit it which is where my tools comes in. My IPMIPWN tool does all the real work for you, it will attempt to exploit the cipher 0 vuln and setup a backdoor account with a semi-random username and random password. This tool does require you to have ipmiutils "apt-get install ipmitool" installed and it works best on Kali.

USAGE: python ipmipwn.py <IP>
