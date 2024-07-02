# MITRE ATT&CK Framework

- The specific behaviors used by the attacker: techniques, tactics, and procedures (TTPs)
- Website: [MITRE ATT&CK®](https://attack.mitre.org/)
- **Reconnaissance**
	- The attacker is looking for victims or ways to get into victims' systems that have been identified.
- **Resource Development**
	- Infrastructure for managing compromised hosts is put together here, as well as developing exploits or collecting credentials from other sources that could be used.
- **Initial Acess**
	- System or user accounts are compromised to provide the attacker access to a resource that can be used.
- **Execution**
	- A series of actions or behaviors an attacker might use to maintain access to the system.
- **Persistence**
	- The attacker needs to ensure they maintain access beyond reboots or other system changes -> Ensure the malware always run when the system is started, or at least when a user logs in.
- **Privilege Escalation**
	- Attackers would typically look to gain administrative privileges = privilege escalation.
- **Defense Evasion**
	- Business will do a lot of work trying to protect systems.
	- Defense evasion means trying to get access and maintain access regardless of the protection measures in place.
- **Credential Access**
	- Gather usrenames and passwords.
- **Discovery**
	- Any activity that collects information within the victim enviroment could be considered discovery.
- **Lateral Movement**
	- Attackers will generally move from one system to another within the victim environment, to collect more information or to gather details about systems or users that could be used elsewhere.
- **Collection**
	- Once the attacker has found information they want to use or sell, they need to pull it together. This is the collection referred to here. It may be something simple like staging the data  somewhere in the network.
- **Command and Control**
	- The attacker needs a way of getting remote access to systems or to send commands to those systems.
	- With firewalls in place, direct access to victim systems is not commonly possible.
	- the connection needs to be initiated from the inside of the network.
- **Exfiltration**
	- Means moving the data our of the target environment.
- **Impact**
	- The types of activities that affects to the victims' system.

[Back to Chapter 1: Ethical Hacking](my-ceh-v12-notes.md#chapter%201%20ethical%20hacking)