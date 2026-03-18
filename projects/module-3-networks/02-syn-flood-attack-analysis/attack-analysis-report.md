# Network Attack Analysis — Incident Report

**Incident:** Web Server Denial of Service
**Organization:** Travel Agency (fictional scenario)
**Analyst:** Security Analyst Intern (Google Cybersecurity Certificate Program)
**Date:** 2024

---

## Section 1: Identify the Type of Attack

### What type of attack occurred?

Based on analysis of the Wireshark TCP log captured during the incident, the attack is identified as a **SYN Flood Attack** — a type of **Denial of Service (DoS)** attack.

### How was the attack identified?

Reviewing the TCP log revealed the following pattern:

- The web server received a high volume of **TCP SYN packets** from a single external IP address in rapid succession
- The server responded to each SYN with a **SYN-ACK** packet, as expected during the TCP three-way handshake
- The external source **never sent the final ACK** to complete the connections
- As a result, the server's **connection table filled up** with half-open connections
- Legitimate visitors attempting to connect to the travel agency's website received **timeout errors** and could not load the page

This pattern — high-volume SYN requests with no completing ACK — is the defining signature of a SYN flood attack.

---

## Section 2: How the Attack Affects the Organization

### Technical Impact

The TCP three-way handshake works as follows under normal conditions:

1. **Client sends SYN** — initiates connection request
2. **Server sends SYN-ACK** — acknowledges and reserves resources for the connection
3. **Client sends ACK** — completes the connection

In a SYN flood, the attacker sends thousands of SYN packets but never completes step 3. The server reserves memory and CPU resources for each half-open connection and holds them for a timeout period. When the connection table is exhausted, the server cannot accept any new connections — including from legitimate users.

### Business Impact

| Impact Area | Description |
|-------------|-------------|
| **Service availability** | The company's website became unreachable to customers |
| **Revenue loss** | Customers could not browse or book travel during the attack window |
| **Reputation damage** | Customers experiencing repeated outages lose trust in the business |
| **Employee productivity** | Staff were unable to access internal web-based systems |
| **Incident response cost** | IT staff diverted from normal operations to investigate and mitigate |

### Duration and Scope

The attack targeted the web server's public-facing port 443 (HTTPS). The server was overwhelmed within minutes of the attack beginning, as the SYN packet rate exceeded the server's connection handling capacity.

---

## Section 3: How to Prevent or Mitigate SYN Flood Attacks

| Control | Description |
|---------|-------------|
| **SYN Cookies** | Server generates a cryptographic cookie instead of allocating resources for half-open connections; resources are only allocated once the ACK is received and verified |
| **Firewall rate limiting** | Configure the firewall to limit the number of SYN packets accepted per second from a single source IP |
| **IDS/IPS rules** | Deploy intrusion detection/prevention rules to identify and block SYN flood patterns in real time |
| **Anycast network diffusion** | Distribute attack traffic across multiple servers (commonly used by CDN providers) |
| **Upstream filtering (ISP-level)** | Work with ISP to filter malicious traffic before it reaches the organization's network |

---

## Section 4: Conclusion

The SYN flood attack successfully disrupted the travel agency's web services by exploiting the TCP handshake process. The attack was relatively simple — requiring no authentication bypass or malware — yet had significant business impact.

Implementing SYN cookies at the network layer, combined with firewall rate limiting and IDS monitoring, would substantially reduce the organization's exposure to this attack type. These controls should be considered foundational network security measures for any public-facing web service.
