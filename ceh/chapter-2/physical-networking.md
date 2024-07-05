# Physical Networking

- Need a network interface on your end.
- Focus on Ethernet.
- The PDU at layer 2 is **frame**.

## Addressing
- Ethernet interfaces all have addresses.
- Exclusive to each network interface, called MAC addresses.
- MAC addresses is hard-coded into the hardware of the interface == hardware address == physical address.
- Format: 6 octets (8-bit bytes), separated by colons. Ex: `BA:00:4C:78:57:00`
- Two parts:
	- OUI: organizationally unique identifier ~ vendor ID
	- Unique address within the vendor ID.
- Represented in hexadecimal values. `00` is `0`, `ff` is 255.
- The broadcast MAC address is used for send messages to every devices in the network, it is `FF:FF:FF:FF:FF:FF`.
## Switching
- A switch == a multiport bridge.
- A bridge is a device that connects two networks together.
- Switch needs to know what MAC address lives at which port.
- **CAM** (Content-addressable memory), uses MAC address as an index value to find which port should it send traffic through.
- Switch limits the capability to do security testing because we cannot see the traffic around the network -> Should tell the switch mirror traffic to one port to another port.

[Back to Chapter 2: Network Foundations](../ceh.md#chapter%202%20network%20foundations)