# Scanning Beyond IDS and Firewall


Muốn scanning beyond Firewall thì phải có sẵn cái gì đó inside target của mình, dùng nó để send data ra bên ngoài (gửi cho mình).

## SSH Tunneling (SSH Port forwarding)

- Secure Shell provides a secure channel between two hosts.
- SSH tunnels allow you to open a local listener that forwards to a remote host through an encrypted session.

### Local Port Forwarding (use for scanning)

E.g. Accessing an online server's database (MySQL, Postgres, Redis, etc.) using a fancy UI tool from your laptop.

```bash
ssh -L [local_addr:]local_port:remote_addr:remote_port [user@]sshd_addr
```

`-L` indicates _local port forwarding_.
![[ssh_local_port_forwarding.png]]

### Remote Port Forwarding

Expose a local service to the outside world, e.g. exposing a dev service from your laptop to the public Internet for a demo.

```bash
ssh -R [remote_addr:]remote_port:local_addr:local_port [user@]gateway_addr
```

`-R` indicates _remote port forwarding_

![[ssh_remote_port_forwarding.png]]
### HTTP proxy

```bash
ssh -D 8888 foo.company.com
```

Then go to browser → Enable proxy connection → Choose `socks4/5`, `host:localhost`, port `8888`.

## HTTP Tunneling

A method of bypassing firewall restrictions by encapsulating data inside HTTP packets.

## Proxy Servers

Proxy servers run special software that accept data and forward it to the correct destination _hiding_ the source behind the proxy server.

`Tor` network.