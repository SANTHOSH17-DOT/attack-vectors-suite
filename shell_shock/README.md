SHELL SHOCK ATTACK
==================

![logo loading](logo.png)

### 🟡 Introduction 😁:

Shellshock is a 30-year old bug in the Bash shell that was discovered as a significant threat in 2014. Despite being less risky today, it still poses a threat to enterprises.With recent shifts in security priorities, it's important to examine Shellshock and the factors that contribute to its continued existence.

  

* * *

### 🟡 How Does Shellshock Work 🙃?

Shellshock is a vulnerability that allows unauthorized execution of commands with higher privileges in systems using vulnerable versions of the Bash shell. This vulnerability occurs due to the execution of unintended bash commands from unsanitized environment variables. Attackers can exploit this vulnerability to remotely issue commands on target hosts, as many services like web servers use environment variables for communication with the OS. To prevent exploitation, input data must be sanitized before execution.

  

* * *

### 🟡 Reports of attacks 🙀

The Bash vulnerability was quickly exploited after its announcement, resulting in compromised machines. Within a day, these machines were used in DDoS attacks and vulnerability scanning by botnets. Reports showed that the attacks originated from multiple countries, including China and the US. By the end of September, 1.5 million daily attacks and probes related to Shellshock were recorded by CloudFlare. However, it was later disputed whether the Yahoo! server attack was specifically due to Shellshock.

  

* * *

### 🟡 Vulnerability 😬:

Shellshock can affect not only web servers, but also email and DNS servers using BASH to communicate with the OS. Unix-based systems are vulnerable, but organizations using Windows-based systems may also be at risk via vulnerable appliances or hardware. BASH is found in home routers, IoT devices, and embedded systems and can even be used to launch DOS attacks. By executing malicious code, attackers can steal confidential data and information stored on the system, launch programs, create connections to their own systems, and execute malicious software. The risk of harmful remote command execution by internet users is high.

* * *

### 🟡 How to know that you are affected 😵‍💫?

Shellshock, a 6-year-old vulnerability in the Bash shell, can be exploited to execute privileged commands, potentially leading to system takeover. To detect the vulnerability, free tools such as bashcheck can be used, or a simple command in the Bash prompt can be executed. If the output returns "Bash is Infected," it's time to update and fix. To test vulnerability in websites or CGI scripts, a "ShellShock" Bash Vulnerability Test Tool can be used. Simply enter the URL and click the button to check for vulnerability.

* * *

### 🟡 How to be Protected 🤔? 

To prevent Shellshock exploitation:

    Monitor and scan systems for vulnerabilities
    Deploy adequate personnel and time for system security maintenance
    Determine the level of vulnerability based on network infrastructure
    Update all firmware/OS and install security updates
    Use vulnerability detection tools, patch systems immediately and closely track network activity
    Use intrusion prevention system if possible
    Ensure third-party vendors take adequate security measures
    Be cautious of phishing attacks, especially for Mac OS users in emails.

  

* * *

### 🟡 Specific Exploitation Vectors 💀

#### ⭐CGI-based web server :

"Bash Shellshock is triggered by a specially crafted document request in web servers using CGI (Common Gateway Interface). The server copies information into environment variables, which can be processed by a handler program, including a Bash script, and exploit the vulnerability. CGI scripts can pose a security risk if not properly checked. Alternatives to CGI include other methods of handling web server requests. Online testing services are available for testing vulnerability of exposed web servers."

#### ⭐OpenSSH server :

"OpenSSH's "ForceCommand" feature executes a fixed command when the user logs in, regardless of their specified command. This can lead to Shellshock exploitation if the forced command runs in a Bash shell, as the environment variable "SSH_ORIGINAL_COMMAND" is parsed and executed on start-up. This allows users with restricted shell access to gain unrestricted access through the Shellshock bug."

#### ⭐DHCP clients :

"DHCP clients are vulnerable to Shellshock when connecting to an open Wi-Fi network. A malicious DHCP server can provide a crafted string in an option, leading to code execution on a vulnerable system."

#### ⭐Qmail server :

"Email processing using Bash (e.g. through .forward or qmail-alias piping) can lead to exploitation of the Shellshock vulnerability if the system is running a vulnerable version of Bash."

#### ⭐IBM HMC restricted shell :

"The IBM Hardware Management Console's restricted shell is vulnerable to the Shellshock bug and can be exploited to gain access to the Bash. IBM has released a patch to fix this vulnerability."

  

* * *

### 🟡 Conclusion 😎:

Organizations must employ a vulnerability management framework to detect, assess, and protect against Shellshock and future vulnerabilities. This framework should quickly identify vulnerabilities, determine their severity, and take necessary action. Effective vulnerability management is a key process in ensuring cyber security. A mature organization should treat the resolution of critical vulnerabilities, such as Shellshock, with the same urgency as a serious security incident.

* * *
### 🟡 Important Keywords 🤓:

Cloudflare - "A web performance and security company"
DNS - "Domain Name System"
DOS - "Disk Operating System"
DHCP - "Dynamic Host Configuration Protocol" 
IBM - "International Business Machines is a tech multinational company"
  

BE ALERT ⚠️ BE SAFE 
-------------------
