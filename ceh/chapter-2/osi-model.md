# Open Systems Interconnection

- 7 layers
- **Application (Layer 7)**
	- Not the application itself.
	- Manage the communication needs of the application.
	- May identify resources and manage interacting with those resources.
	- Example: Hypertext Transfer Protocol (HTTP) takes care of negotiating for resources (pages, etc.) between client and the server.
- **Presentation (Layer 6)**
	- Preparing data for the Application Layer.
	- Makes sure data is handed up to the application in the right format.
	- ASCII, Unicode, Extended Binary Coded Decimal Interchange Code (EBCDIC)
	- Joint Photographic Experts Group (JPEG) format is considered to be at the Presentation layer.
- **Session (Layer 5)**
	- The Application layer takes care of managing the resources while the Session layer takes care of making sure that files, as an example, are successfully transmitted and complete.
	- Manages the communication between the endpoints.
- **Transport (Layer 4)**
	- Takes care of segmenting messages for transmission.
	- Takes care of multiplexing of the communication.
	- TCP, UDP
	- Use ports for addressing
- **Network (Layer 3)**
	- Gets messages from one endpoint to another.
	- Take care of addressing and routing.
	- IP protocol.
- **Data Link (Layer 2)**
	- Media Access Control (MAC) address.
	- Identify the network interface on the network so communications can get from one system to another on the local network.
	- ARP (Address Resolution Protocol), VLANs (Virtual local area networks), Ethernet, Frame Relay
	- Take care of formatting the data to be sent out on the transmission medium.
- **Physical (Layer 1)**
	- 10BaseT, 10Base2, 100BaseTX, 1000BaseT

> [!warning]
> Not always food fits when it comes to mapping protocol to the seven layers. Especially between the Session and Application layers.

[Back to Chapter 2: Network Foundations](../ceh.md#chapter-2-network-foundations)
