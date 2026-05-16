# Describing Network Communication with Models

Source: closed course page  
Date added: 2026-05-16  
Related plan item: Week 3 / Describing communication with OSI  
Tags: osi, encapsulation, tcp, udp, ports, ip address, mac address, physical layer, troubleshooting
Language: English
Translation pair: articles/2026-05/week-03/04-describing-network-communication-with-models.md

## Summary

One browser click starts a full network communication chain. The request moves down the OSI layers: the application creates the request, data is formatted, the session is separated from other conversations, transport adds TCP/UDP behavior and ports, network adds IP addresses, data link adds MAC addresses, and the physical layer turns everything into electrical signals, light or radio waves.

The NetworkChuck Coffee mocha request shows that the OSI model is not just a list of layers. It is a practical way to describe the real path data takes through a network.

## Key Points

- A browser click can be described through all seven OSI layers.
- Layer 7 is where network-aware applications operate.
- Encapsulation means each layer wraps data with its own header or information.
- Presentation layer formats data using standards such as HTTP or HTTPS.
- Session layer helps separate different conversations on the same machine.
- Transport layer chooses TCP or UDP.
- TCP is reliable and uses acknowledgments.
- UDP is faster and does not wait for every lost packet to be recovered.
- Port numbers identify the application or service conversation.
- HTTPS commonly uses destination port 443.
- Network layer adds source and destination IP addresses.
- Data Link layer uses MAC addresses for hop-to-hop delivery.
- IP addresses usually stay end-to-end, while MAC addresses change at each router hop.
- Physical layer converts bits into electrical signals, light pulses or radio waves.
- The receiving side decapsulates the data in reverse order.

## Notes

### One Click, Seven Layers

Imagine NetworkChuck Coffee.

An employee opens a browser on the back-office computer and clicks the Mocha button to retrieve a recipe from the central repository.

For the user, that is one click.

For the network, it is a trip through the OSI model:

```text
Application -> Presentation -> Session -> Transport -> Network -> Data Link -> Physical
```

On the other side, the server receives the data and unpacks it in reverse order.

### Layer 7 - Application

The Application layer is where a network-aware application begins communication.

Examples:

- Chrome;
- Firefox;
- Edge;
- email client;
- API client;
- file transfer application.

Important: not every application is automatically a network application. If a program does not talk to another device, it is not participating in network communication.

In this example, the browser creates the request:

```text
Give me the mocha recipe.
```

### Layer 6 - Presentation

The Presentation layer is responsible for format, representation and sometimes encoding/encryption concepts.

In a practical web example, the browser uses server-understandable standards:

- HTTP;
- HTTPS.

The simple idea: the request must be formatted in a way the server understands.

### Encapsulation

Encapsulation is the process where each layer adds its own control information to the data.

You can picture it like this:

```text
Original data
Data + Transport header
Data + Transport header + IP header
Data + Transport header + IP header + MAC header
Bits on the wire
```

At each layer, the data receives a new wrapper needed for delivery.

### Layer 5 - Session

The Session layer helps manage separate conversations.

On one computer, several things may run at once:

- browser;
- Spotify;
- email client;
- chat application;
- background updates.

The network stack needs to keep track of which response belongs to which conversation.

In real TCP/IP networks, much of this practical sorting is handled by the transport layer and port numbers, but the OSI model separates the session management idea conceptually.

### Layer 4 - Transport

The Transport layer chooses transport behavior:

- TCP;
- UDP.

TCP is reliable. It expects acknowledgments and tries to deliver data completely and in order.

UDP is unreliable in the technical sense: it does not require an acknowledgment for every packet and does not provide TCP-style recovery logic.

Unreliable does not mean "bad." It means "does not guarantee delivery at the transport protocol level."

### TCP vs UDP

TCP is useful for:

- web browsing;
- login forms;
- file downloads;
- transactions;
- situations where missing data is unacceptable.

UDP is useful for:

- live video;
- voice traffic;
- gaming;
- time-sensitive traffic.

If a live stream loses a packet, it is often better to keep moving than to pause the video and wait for an old fragment to be resent.

### Port Numbers

Port numbers help identify which application conversation traffic belongs to.

There are 65,536 port numbers:

```text
0 through 65535
```

Well-known ports are below 1024.

Example:

```text
HTTPS: TCP port 443
SMTP: TCP port 25
```

When the browser sends the mocha request:

```text
Source port: 55192
Destination port: 443
```

When the server responds:

```text
Source port: 443
Destination port: 55192
```

That is how the computer knows the response belongs to the browser, not Spotify or another application.

### Why Ports Matter in Troubleshooting

When a service "is not responding," a good question is:

```text
Is the right port open?
```

Firewalls often allow or block traffic based on port numbers.

If an HTTPS service should respond on port 443 but the firewall blocks 443, the problem may be in the path or policy, not the application.

### Layer 3 - Network

The Network layer adds source and destination IP addresses.

An IP address is an end-to-end address.

Analogy: the final destination city on a travel itinerary.

Example:

```text
Source IP: back-office computer
Destination IP: central coffee server
```

IP helps identify where the packet comes from and where it ultimately needs to go.

### Layer 2 - Data Link

The Data Link layer uses MAC addresses.

A MAC address works hop-to-hop.

That means:

- the MAC address helps reach the next device;
- at each router, the old Layer 2 header is removed;
- a new Layer 2 header is added for the next segment;
- the source/destination IP addresses usually remain the same end-to-end.

Simple idea:

```text
IP gets you to the final destination.
MAC gets you to the next hop.
```

### IP vs MAC

The difference:

| Address Type | Scope | Changes at Router? | Used By |
| --- | --- | --- | --- |
| IP address | End-to-end | Usually no | Layer 3 |
| MAC address | Hop-to-hop | Yes | Layer 2 |

Traceroute helps reveal the route as multiple hops. It shows that a path across the internet is not one jump, but a sequence of routers.

### Layer 1 - Physical

The Physical layer turns data into a real signal.

Depending on the medium, that can be:

- electrical signals on copper;
- pulses of light on fiber;
- radio waves over Wi-Fi.

At the bottom, it is just bits:

```text
1s and 0s moving across a medium
```

### Decapsulation

When the request reaches the central coffee server, the process reverses.

The server unpacks the data upward:

```text
Physical -> Data Link -> Network -> Transport -> Session -> Presentation -> Application
```

Each layer reads its own information, removes its wrapper and passes the payload upward.

Then the server sends the response with the mocha recipe back using the same principle.

### Why This Matters

This model helps show that network communication is not magic.

One click involves:

- application request;
- formatting;
- session/conversation tracking;
- TCP or UDP behavior;
- port numbers;
- IP addressing;
- MAC addressing;
- physical signaling.

The better you see this process, the easier IP addressing, routing, switching and troubleshooting become later.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Encapsulation | Process where each layer wraps data with its own header or control information. |
| Decapsulation | Reverse process where the receiver removes layer information and passes data upward. |
| HTTP | Web protocol used for browser/server communication without built-in encryption. |
| HTTPS | Secure web protocol commonly using TCP port 443. |
| TCP | Reliable transport protocol that uses acknowledgments and ordered delivery. |
| UDP | Transport protocol that sends data without TCP-style delivery guarantees. |
| Port number | Transport-layer identifier for a service or application conversation. |
| Well-known port | Port number below 1024 commonly assigned to standard services. |
| Source port | Port used by the sending side for a specific conversation. |
| Destination port | Port the sender targets on the receiving side. |
| IP address | Layer 3 address used for end-to-end delivery between networks. |
| MAC address | Layer 2 address used for hop-to-hop delivery on a local segment. |
| Traceroute | Tool that shows the router hops along a path to a destination. |
| Physical medium | Copper, fiber or wireless space used to carry bits. |

## Questions

### 1. What happens when the user clicks the Mocha button in the browser?

The browser creates a network request that travels down the OSI layers, gets encapsulated at each layer and is sent to the server.

### 2. What is encapsulation?

It is the process where each layer adds its own control information, such as a transport header, IP header or MAC header.

### 3. Which layer uses TCP and UDP?

The Transport layer, Layer 4.

### 4. How is TCP different from UDP?

TCP is reliable and uses acknowledgments. UDP does not guarantee delivery the same way, but is useful for time-sensitive traffic.

### 5. Why does video streaming often use UDP?

Because live traffic often needs to keep moving instead of waiting for an old lost packet to be resent.

### 6. What are port numbers for?

They identify the service or application conversation, such as HTTPS on port 443.

### 7. What does destination port 443 indicate?

It indicates the client is trying to reach an HTTPS service on the server.

### 8. Why does the server response return to a random high-numbered client port?

Because the client used that source port for the specific browser conversation, so the operating system knows which application should receive the response.

### 9. What does the Network layer add?

Source and destination IP addresses.

### 10. How is an IP address different from a MAC address?

An IP address is used end-to-end, while a MAC address is used hop-to-hop and changes at each router segment.

### 11. What does the Physical layer do?

It converts bits into electrical signals, light pulses or radio waves.

### 12. What is decapsulation?

It is the reverse process on the receiving side, where each layer removes its header or wrapper and passes the data upward.

## What To Review Later

- Encapsulation and decapsulation.
- Seven OSI layers in order.
- TCP vs UDP.
- Port numbers and well-known ports.
- HTTPS port 443.
- IP address vs MAC address.
- Hop-to-hop vs end-to-end delivery.
- Physical media: copper, fiber and Wi-Fi.
