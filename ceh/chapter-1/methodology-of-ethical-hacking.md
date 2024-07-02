# Methodology of Ethical hacking

- Reproduce what real-life attackers would do.
- **Reconnaissance and Footprinting**
	- Gather information about your target.
	- Objective: determining the size and scope of your test.
	- Identifies network blocks, single hosts.
- **Scanning and Enumeration**
	- Identify services running on any available host. These services will be used as entry points -> Gather open ports and the service and software running behind each open port.
	- Gather as much information as you can.
	- Can be time-consuming.
- **Gaining Access**
	- Exploiting the services to get access to systems.
	- Need demonstrate or prove in some way that you did manage to compromise the system -> *documentation*.
- **Maintaining Access**
	- Create a backdoor.
	- Use some malware.
	- Often called: *persistence*.
	- Objective: no matter whether a user logs out or reboots a system, the attacker can continue to get in.
	- System:
		- Inbound access is often blocked by a firewall.
		- Outbound access is often allowed from the inside of a network in a completely unrestricted manner.
- **Covering Tracks**
	- Hide or delete any evidence to which you managed to get access. Additionally, cover up your continued access.

[Back to Chapter 1: Ethical Hacking](my-ceh-v12-notes.md#chapter%201%20ethical%20hacking)