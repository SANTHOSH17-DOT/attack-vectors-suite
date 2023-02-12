TCP attacks
===========

### 🔵 What is TCP Attack ?

📌 The TCP Reset Attack is a method of disrupting communication by sending fake TCP reset packets to a host.

📌 This common attack on the Internet often targets non-cooperative websites and can be used to launch DDoS attacks.

* * *

### 🔵 How a TCP Attack Works ?

📌 In a normal TCP connection, the sending computer sends a TCP reset packet (RST) to the receiving computer if it's not actively listening for communication.

📌 This occurs when the receiving computer hasn't sent an acknowledgment in a while. 

📌 However, in a TCP Reset Attack, the sending computer sends a fake RST packet to disrupt communication.
  

* * *

### 🔵 How to mitigate such an attack ?

📌 Servers are still vulnerable to SYN flood attacks despite the improved management of resources in current operating systems.

📌 Common mitigation techniques include micro blocks, SYN cookies, RST cookies and stack tweaking. 

📌 Micro blocks allocate a small record in memory for each incoming request, SYN cookies involve responding to requests with a SYN-ACK but dropping the SYN from memory, RST cookies send an invalid SYN-ACK to verify requests, and stack tweaking involves modifying TCP stacks to drop incoming connections or release memory. 

📌 All of these strategies require the ability to handle high volume DDoS attacks in the Gigabit range.

* * *

### 🔵 Background

📌 The Internet is a global network of computers that communicate with each other using protocols like IP, TCP and UDP. 

📌 The Internet Protocol (IP) is the foundation for data transfer on the Internet, while the Transmission Control Protocol (TCP) is used to establish a two-way, reliable communication between devices.

📌 When two computers need to exchange data, they use a TCP/IP socket to send a stream of packets.
 
📌 This protocol provides a reliable connection-oriented transfer, which is useful for large files like video clips or email attachments. 

📌 Web browsing also uses TCP/IP to ensure the reliable transfer of web pages, even if they are small enough to fit in a single packet.

📌 FUN FACT😃 - When we see a message of "Session expired" on a banking site or college site, then it is beacause long duration connection make sites more vulnerable to attacks. 

* * *
