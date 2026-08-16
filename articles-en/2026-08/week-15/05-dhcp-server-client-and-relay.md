# DHCP Server Client And Relay

Source: closed course page  
Date added: 2026-08-16  
Related plan item: Week 15 / DHCP server client and relay  
Tags: DHCP, DORA, DHCP server, DHCP client, DHCP relay, ip helper-address, Cisco IOS, troubleshooting
Language: English
Translation pair: articles/2026-08/week-15/05-dhcp-server-client-and-relay.md

## Summary

- DHCP feels automatic until devices stop receiving IP addresses.
- On Cisco devices, DHCP appears in three roles: server, client, and relay agent.
- A DHCP server gives out IP settings from a pool.
- A DHCP client requests an address and network parameters.
- A DHCP relay agent forwards requests to a DHCP server in another subnet.
- The core DHCP process is DORA: Discover, Offer, Request, Acknowledge.
- On Cisco, relay is usually configured with `ip helper-address`.

## Key Points

- DHCP provides more than an IP address: default gateway, DNS servers, lease time, and other options.
- Configure excluded addresses before building the DHCP pool.
- A router is often a convenient DHCP server in small and midsize networks.
- A switch management interface can be a DHCP client, especially in labs or staging.
- In production, infrastructure devices often use static management IPs for predictability.
- DHCP broadcasts do not cross routers by themselves.
- If the DHCP server is in another subnet, relay is required.

## Notes

DHCP, or Dynamic Host Configuration Protocol, works so well that it is easy to ignore. A device connects, receives an address, gateway, DNS, and starts working.

Then one day the address does not arrive.

At that point, DHCP stops being background plumbing and becomes a critical service. At NetworkChuck Coffee, barista tablets, office PCs, POS terminals, and management interfaces without addresses cannot participate in the network correctly.

Main idea:

```text
DHCP is invisible while it works. When it breaks, the network quickly feels broken.
```

## DHCP Roles

Keep three roles in mind.

| Role | Function |
| --- | --- |
| DHCP server | Gives IP settings to clients. |
| DHCP client | Requests settings. |
| DHCP relay agent | Forwards DHCP requests between subnets. |

On Cisco routers, all three ideas can appear:

- a router can hand out addresses as a DHCP server;
- a switch or router interface can receive an address as a DHCP client;
- a router interface can forward DHCP requests with `ip helper-address`.

## Cisco Router As DHCP Server

In small and midsize networks, the router is often a convenient DHCP server.

It already:

- knows the local subnets;
- handles routing;
- is often the default gateway;
- is required for site operation.

Basic configuration logic:

1. Exclude static addresses.
2. Create a DHCP pool.
3. Define the network.
4. Define the default router.
5. Define the DNS server.
6. Add domain name and other options if needed.

Example:

```text
ip dhcp excluded-address 192.168.10.1 192.168.10.20

ip dhcp pool CAFE-VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.10.53
 domain-name cafe.local
```

Configure `excluded-address` before the pool. Those addresses should not be handed to clients because they are reserved for gateways, servers, printers, or other static devices.

Technically, the router should not hand out its own address, but explicit exclusions are still good practice. They make the design clearer for the next administrator.

## The DORA Process

DORA is the basic DHCP conversation.

| Step | What happens |
| --- | --- |
| Discover | Client broadcast: "I need an IP address." |
| Offer | Server offers an address and options. |
| Request | Client selects the offer and requests it. |
| Acknowledge | Server confirms the lease and settings. |

Simplified:

```text
Discover -> Offer -> Request -> Acknowledge
```

If multiple DHCP servers exist, the client may receive multiple offers. It usually chooses the first answer.

DHCP does not only provide an IP address. It tells the device where it lives and how to communicate.

The client commonly receives:

- IP address;
- subnet mask;
- default gateway;
- DNS server;
- lease time;
- additional options.

## DHCP Client On A Network Device

A DHCP client is not only a laptop or desktop.

A Cisco switch can use DHCP on a management interface, such as an SVI.

Example idea:

```text
interface vlan 10
 ip address dhcp
 no shutdown
```

This is useful:

- in labs;
- during staging;
- in temporary networks;
- for quick deployment.

But static IP is often better for production management.

Why:

- easier documentation;
- easier monitoring;
- easier remote access;
- fewer surprises after lease changes;
- more predictable troubleshooting.

Rule: know DHCP client mode, but use it intentionally for infrastructure management.

## When The Server Is In Another Subnet

DHCP begins with a broadcast.

Problem:

```text
Routers do not forward broadcasts by default.
```

If a client in VLAN 10 sends a DHCP Discover and the DHCP server is in VLAN 50, the request will not cross the router by itself.

That requires a DHCP relay agent.

On Cisco, the usual command is:

```text
interface vlan 10
 ip helper-address 192.168.50.10
```

It tells the router or Layer 3 switch:

```text
When you hear DHCP requests in this VLAN, forward them to that remote DHCP server.
```

## How Relay Helps Server Pool Selection

Relay does not forward blindly.

It includes information about where the request came from. That lets the centralized DHCP server choose the correct scope.

Example:

- the request arrived on interface VLAN 10;
- the server sees that it belongs to the VLAN 10 subnet;
- the server selects the VLAN 10 DHCP pool;
- the offer returns through the relay.

Without that detail, the server would not know which address pool to use.

In a large network, this matters. You do not need a separate DHCP server in every VLAN. You can centralize DHCP infrastructure and use relay on gateway interfaces.

## DHCP Troubleshooting

Good questions beat random commands.

Ask:

1. Is the client sending Discover?
2. Is the server responding with Offer?
3. Is the client in the correct subnet?
4. Is the DHCP pool configured correctly?
5. Do excluded addresses consume too much of the pool?
6. Are default gateway and DNS options correct?
7. If the server is remote, is `ip helper-address` present?
8. Is there routing between relay and DHCP server?
9. Is an ACL blocking DHCP traffic?
10. Is there a rogue DHCP server?

If you understand DORA, troubleshooting becomes a conversation: where did the dialogue stop?

## NetworkChuck Coffee Scenario

NetworkChuck Coffee needs DHCP for:

- tablets;
- POS terminals;
- office PCs;
- guest devices;
- printers;
- switch management in labs;
- new site deployment.

For a small site, the router can be the DHCP server:

```text
ip dhcp pool CAFE
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.10.53
```

If a centralized server later appears in the back office or data center, VLAN gateway interfaces get `ip helper-address`.

That keeps DHCP centralized while still serving many VLANs.

## Verification

Useful commands:

```text
show ip dhcp pool
show ip dhcp binding
show ip dhcp conflict
show running-config | section dhcp
show running-config interface vlan 10
debug ip dhcp server packet
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp pool CAFE-VLAN10
ip helper-address 192.168.50.10
```

Check:

- the pool exists;
- network and mask are correct;
- default-router is correct;
- DNS server is correct;
- excluded range is not too large;
- bindings appear;
- conflicts are absent or explainable;
- helper address is configured on the correct interface;
- the client is really in the expected VLAN.

## Main Takeaway

DHCP feels simple because most of the time it works by itself.

Behind that simplicity are three important roles: server, client, and relay agent. The server gives settings, the client requests them, and relay carries requests across a router boundary.

If you know DORA and understand `ip helper-address`, you can do more than configure DHCP. You can quickly identify exactly where address assignment broke.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| DHCP | Dynamic Host Configuration Protocol, automatic IP setting assignment. |
| DORA | Discover, Offer, Request, Acknowledge. |
| DHCP server | Device that provides IP settings. |
| DHCP client | Device that requests IP settings. |
| DHCP relay agent | Device that forwards DHCP requests to a server in another subnet. |
| `ip dhcp pool` | Creates a DHCP pool on a Cisco device. |
| `ip dhcp excluded-address` | Excludes addresses from DHCP assignment. |
| `default-router` | DHCP option for the default gateway. |
| `dns-server` | DHCP option for the DNS server. |
| `ip helper-address` | Cisco command for DHCP relay. |
| lease | Temporary assignment of IP settings to a client. |
| scope | Address pool on a DHCP server for a specific subnet. |

## Questions

### 1. Which three DHCP roles matter on Cisco devices?

Answer: DHCP server, DHCP client, and DHCP relay agent.

### 2. What does DORA mean?

Answer: Discover, Offer, Request, Acknowledge.

### 3. Why configure excluded addresses early?

Answer: To prevent the DHCP server from handing out addresses reserved for gateways, servers, printers, or other static devices.

### 4. Why use `ip helper-address`?

Answer: To forward DHCP requests from one subnet to a DHCP server in another subnet.

### 5. Why is DHCP client mode on a switch management interface not always the best production design?

Answer: Static management IPs are usually easier to document, monitor, and use for remote access.

## What To Review Later

- DORA process.
- `ip dhcp excluded-address` configuration.
- `ip dhcp pool` configuration.
- DHCP options `default-router` and `dns-server`.
- DHCP client on an SVI.
- DHCP relay with `ip helper-address`.
- `show ip dhcp binding` verification.
