# Network Architectures

- Topology + data flows + other network elements = Network Architectures

## Network Types
- **Local Area Network (LAN)**
    - Probably in the same room or building or on the same floor.
    - Would be in the same broadcast domain or collision domain -> communicate using layer 2 without having to route to other networks.
- **Virtual Local Area Network (VLAN)**
    - is a LAN where the isolation at layer 2 is handled by software/firmware.
- **Wide Area Network (WAN)**
    - whose nodes are more than 10 or so miles apart.
    - Any Internet service provider would have a WAN.
- **Metropolitan Area Network (MAN)**
    - Between a LAN and a WAN.

## Isolation

- Common approach: **DMZ** (Demilitarized zone)
- **DMZ** isolates untrusted systems from the remainder of network.
- An untrusted system: anyone from the Internet can get access to.
- Common way of protecting highly sensitive information: use enclaves.
- Enclave: an isolated network segment where tight controls may be placed.
- Microsegmentation: segments are defined based on workload. Use in virtual enviroment.

## Remote Access
- **VPNs** (Virtual private networks): a way to gain access to the internal network from remote locations.
- **MPLS** (Multiprotocol Label Switching): provides what is essentially a tunnel from one location to another by encapsulating traffic inside a label.
- **IPSec** (IP Security) is a set of extensions provide for encryption from one location to another.

[Back to Chapter 2: Network Foundations](../ceh.md#chapter-2-network-foundations)