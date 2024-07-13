# HTB - SolarLab
https://app.hackthebox.com/machines/SolarLab

Target IP: 10.10.11.16

Nmap scan:
PORT    STATE SERVICE
80/tcp  open  http
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

PORT    STATE SERVICE       VERSION
80/tcp  open  http          nginx 1.24.0
|_http-title: Did not follow redirect to http://solarlab.htb/
|_http-server-header: nginx/1.24.0
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2024-07-13T07:28:45
|_  start_date: N/A
|_clock-skew: -7m47s
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled but not required

Add host to `/etc/hosts`: 10.10.11.16 solarlab.htb

The website has nothing fun.

Scan for vhost?

ffuf -u http://solarlab.htb -H "Host: FUZZ.solarlab.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -mc 200 -fc 404 -t 40

No vhost found.

ffuf -u https://FUZZ.solarlab.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -v -c -t 40

Enumerate SMB:

Enumerate SMB Shares using Nmap
nmap -p 445 --script smb-enum-shares,smb-enum-users 10.10.11.16

nothing.

List Shares with smbclient
smbclient -L //10.10.11.16 -N

Sharename       Type      Comment
---------       ----      -------
ADMIN$          Disk      Remote Admin
C$              Disk      Default share
Documents       Disk
IPC$            IPC       Remote IPC

smbclient //10.10.11.16/Documents -N

Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Fri Apr 26 10:47:14 2024
  ..                                 DR        0  Fri Apr 26 10:47:14 2024
  concepts                            D        0  Fri Apr 26 10:41:57 2024
  desktop.ini                       AHS      278  Fri Nov 17 05:54:43 2023
  details-file.xlsx                   A    12793  Fri Nov 17 07:27:21 2023
  My Music                        DHSrn        0  Thu Nov 16 14:36:51 2023
  My Pictures                     DHSrn        0  Thu Nov 16 14:36:51 2023
  My Videos                       DHSrn        0  Thu Nov 16 14:36:51 2023
  old_leave_request_form.docx         A    37194  Fri Nov 17 05:35:57 2023

Downloaded two file: details-file.xlsx old_leave_request_form.docx