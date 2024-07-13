# Communication Models

- Are broken into layers, and the layers are stacked on top of one another.
- Network stacks or protocol stacks
- The layer/function that generated this set of headers on the sending side can be read only by the same layer/function on the receiving side.
- A *protocol* is a set of rules or conventions that dictate communication.
- There are two models:
	- [OSI model](osi-model.md)
	- [TCP/IP Architecture/Model](tcp-ip-architecture.md)
- Each layer of the network stack has a different term to refer to the chunk of data encapsulated by that layer.
- These chunks are called *protocol data units* (PDUs).

[Back to Chapter 2: Network Foundations](../ceh.md#chapter-2-network-foundations)