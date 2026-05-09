# Client & Servers

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Client-server basics  
Tags: client, server, endpoint, switch, access point, network communication, plex, cameras

## Summary

The network is not the main character. It is the infrastructure that lets devices communicate so the business can actually function. At NetworkChuck Coffee, the network exists so phones, laptops, cameras, access points and servers can exchange data reliably.

Main idea: many network conversations follow the client/server model. A client asks for something, a server provides it, and both are endpoints using the network as the path between them.

## Key Points

- The network is infrastructure, not the reason the business exists.
- The goal of networking is communication between devices and services.
- Client/server is a core relationship behind many network interactions.
- A client is the device or application asking for something.
- A server is the device or application providing something.
- One device makes a request, another device responds.
- A phone streaming from a local media server is a client.
- A Plex/media box serving the movie is a server.
- A camera can also act as a client if it sends video to a storage/video server.
- Clients are not only laptops and phones.
- Servers are not only giant data center machines.
- Endpoint is a broad term for devices that sit at the edge of the network and communicate across it.
- Both clients and servers are endpoints.
- Switches, cabling and access points are infrastructure that support endpoint communication.
- Troubleshooting should start by identifying the client, the server and the path between them.

## Notes

### The Network Is Not the Goal

Network engineers care about switches, cables, ports and blinking lights, but the business does not exist for those things.

The network exists to support business needs:

- streaming media;
- storing surveillance footage;
- serving customers;
- processing work;
- connecting devices;
- keeping services available.

At NetworkChuck Coffee, a switch closet matters because it lets real devices do real work.

### Network as Infrastructure

The network is like a road.

It is not the destination. It is the path that lets communication happen.

Simple model:

```text
Device/service needs to talk -> network carries the conversation
```

If you only look at the infrastructure, you can miss the purpose of the traffic.

### Building the Inside Picture

Inside the coffee shop:

- a switch lives in the network closet;
- cables run from the switch to devices;
- a wireless access point connects to the switch;
- phones, tablets and laptops join through WiFi;
- servers or storage systems may connect by cable;
- cameras may send video over the network.

The topology matters, but the communication relationships matter even more.

### Access Point and Switch Path

A wireless device is still using the wired network behind the scenes.

Example path:

```text
Phone -> WiFi -> access point -> switch -> server
```

The phone may feel wireless, but its traffic usually flows through wired infrastructure after it reaches the access point.

### Client/Server Pattern

The client/server relationship is one of the most important patterns in networking.

Core idea:

```text
Client asks.
Server provides.
```

Or:

```text
Client -> request -> server
Server -> response/data -> client
```

Once you see this pattern, network traffic becomes easier to reason about.

### What Is a Client?

A client is the device or application asking for something.

Examples:

- phone requesting a video;
- laptop opening a web page;
- tablet connecting to an internal app;
- camera sending footage to storage;
- POS terminal reaching a server;
- printer client requesting a print service.

The client starts or initiates the interaction.

### What Is a Server?

A server is the device or application providing something.

Examples:

- media server providing a movie;
- file server providing files;
- web server providing a website;
- database server providing data;
- video server receiving/storing footage;
- authentication server validating logins.

The server responds to requests or receives data for a service.

### Media Streaming Example

At NetworkChuck Coffee, imagine a phone wants to watch a movie stored locally.

Roles:

| Device | Role | Why |
| --- | --- | --- |
| Phone | Client | It requests the movie |
| Plex/media box | Server | It stores and sends the movie |
| AP/switch | Infrastructure | They carry the traffic |

Traffic path:

```text
Phone -> AP -> switch -> media server
Media server -> switch -> AP -> phone
```

This makes the traffic less abstract. It is not just "packets"; it is a request and a response.

### Not Every Client Looks Like a Laptop

Clients are not only user devices.

A client is any device/application that initiates a request or sends data to another system.

That means a security camera can be a client.

Why?

```text
Camera sends video to a video/storage server.
```

The camera is the device initiating/sending the data in that relationship.

### Surveillance Example

At NetworkChuck Coffee, cameras may send footage to a video server.

Roles:

| Device | Role | Why |
| --- | --- | --- |
| Camera | Client | Captures and sends video |
| Video/storage server | Server | Receives and stores footage |
| Switch/cabling | Infrastructure | Carries the video traffic |

Different use case, same client/server pattern.

### Troubleshooting Mindset

Instead of starting with:

```text
Is the network broken?
```

Start with:

```text
Who is the client?
What server is it trying to reach?
What path should traffic take?
```

This narrows the problem quickly.

Useful troubleshooting questions:

- Which device is asking?
- Which service is being requested?
- Which server should respond?
- Can the client reach the network?
- Can the server reach the network?
- Is the path between them working?
- Is the issue with the endpoint, infrastructure or service?

### Endpoint

Endpoint is a broad term for devices at the edge of the network that communicate across it.

Endpoints can include:

- phones;
- laptops;
- tablets;
- printers;
- cameras;
- servers;
- POS terminals;
- smart TVs;
- storage systems.

Important:

```text
Both clients and servers are endpoints.
```

Endpoint does not only mean a user device.

### Infrastructure vs Endpoints

Network infrastructure includes:

- switches;
- cabling;
- access points;
- routers;
- firewalls;
- patch panels.

Endpoints use that infrastructure.

Examples:

| Infrastructure | Endpoint |
| --- | --- |
| Switch | Phone |
| Access point | Laptop |
| Cabling | Camera |
| Router | Server |

Network engineers care for the infrastructure so endpoints can work.

### Communication Platform

The network is a communication platform.

Inside the coffee shop, we do not just have connected gadgets.

We have:

- clients making requests;
- servers providing services;
- endpoints relying on infrastructure;
- traffic moving through switches and APs;
- business functions depending on reliable communication.

This is what gives a network diagram purpose.

### Main Takeaway

When looking at traffic, ask:

```text
Who is asking?
Who is providing?
What infrastructure carries the conversation?
```

Client/server explains the relationship.

The network carries the conversation.

Endpoints are the devices and systems participating in it.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Client | Device or application that asks for something or initiates communication. |
| Server | Device or application that provides a service or responds to requests. |
| Endpoint | Device/system at the edge of the network that communicates across it. |
| Infrastructure | Network components that carry traffic, such as switches, cabling and APs. |
| Switch | Device that connects wired LAN devices. |
| Access point | Device that extends the wired network into WiFi. |
| Service | Function provided by a server, such as files, media, web, storage or authentication. |
| Request | Message from a client asking for something. |
| Response | Data or answer sent back by a server. |
| Plex/media server | Example of a server that stores and streams media. |
| Video server | System that receives and stores surveillance footage. |

## Questions

### 1. Why is the network not the main character?

Because the network is infrastructure. Its purpose is to let devices and services communicate so the business can function.

### 2. What is the client/server model?

It is a relationship where one device or application asks for something and another provides it.

### 3. What is a client?

A client is the device or application making a request or initiating communication.

### 4. What is a server?

A server is the device or application providing a service or responding to requests.

### 5. In the media streaming example, what is the client?

The phone is the client because it requests the movie.

### 6. In the media streaming example, what is the server?

The Plex/media box is the server because it stores and sends the movie.

### 7. Can a camera be a client?

Yes. If it sends video to a video/storage server, it is acting as the client in that relationship.

### 8. What is the server in the camera example?

The video/storage server that receives and stores the footage.

### 9. What is an endpoint?

An endpoint is a device or system at the edge of the network that communicates across it.

### 10. Are servers endpoints?

Yes. Both clients and servers can be endpoints.

### 11. What devices can be endpoints?

Phones, laptops, printers, cameras, servers, POS terminals, tablets and other devices using the network.

### 12. What is the role of the switch and access point in client/server communication?

They are infrastructure that carry the traffic between endpoints.

### 13. What troubleshooting question should you ask first?

Who is the client, and what server is it trying to reach?

### 14. Why does identifying client and server help troubleshooting?

It narrows the problem by showing who is requesting, who should respond and what path traffic should take.

### 15. What does the network carry in this model?

The network carries the conversation between clients and servers.

## What To Review Later

- Network as infrastructure, not the business goal.
- Client asks, server provides.
- Request and response.
- Phone/media server example.
- Camera/video server example.
- Endpoint meaning.
- Clients and servers are both endpoints.
- Infrastructure vs endpoints.
- Troubleshooting by identifying client, server and path.
