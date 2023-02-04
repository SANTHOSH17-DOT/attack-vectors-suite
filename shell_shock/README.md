SHELL SHOCK ATTACK
==================

![logo loading](logo.png)

### 🟡 Introduction:

Shellshock is a bug in the Bash command-line interface shell that has existed for 30 years and was discovered as a significant threat in 2014. 

Today, Shellshock still remains a threat to enterprise. The threat is certainly less risky than in the year of discovery. 

However, in a year in which security priorities have recalibrated to keep up with the chaotic landscape, it’s a good time to look back at this threat and the underlying factors that keep these attacks alive today.

  

* * *

### 🟡 How Does Shellshock Work?

Shellshock is a vulnerability that allows systems containing a vulnerable version of Bash to be exploited to execute commands with higher privileges. 

This allows attackers to potentially take over that system. Diving deeper into the technical, Shellshock is a security bug in the Bash shell (GNU Bash up to version 4.3) that causes Bash to execute unintentional bash commands from environment variables. 

Threat actors exploiting the vulnerability can issue commands remotely on the target host.

While Bash is not inherently Internet-facing, many internal and external services such as web servers do use environment variables to communicate with the server’s operating system.

If those data inputs are not sanitized — the coding standard process that ensures that code is not part of the input — before execution, attackers may launch HTTP request commands executed via the Bash shell.

  

* * *

### 🟡 Reports of attacks

Within an hour of the announcement of the Bash vulnerability, there were reports of machines being compromised by the bug. 

By 25 September 2014, botnets based on computers compromised with exploits based on the bug were being used by attackers for distributed denial-of-service (DDoS) attacks and vulnerability scanning.

Kaspersky Labs reported that machines compromised in an attack, dubbed "Thanks-Rob", were conducting DDoS attacks against three targets, which they did not identify.

On 26 September 2014, a Shellshock-related botnet dubbed "wopbot" was reported, which was being used for a DDoS attack against Akamai Technologies and to scan the United States Department of Defense On 26 September, the security firm Incapsula noted 17,400 attacks on more than 1,800 web domains, originating from 400 unique IP addresses, in the previous 24 hours; 55% of the attacks were coming from China and the United States.

By 30 September, the website performance firm CloudFlare said it was tracking approximately 1.5 million attacks and probes per day related to the bug. 

On 6 October, it was widely reported that Yahoo! servers had been compromised in an attack related to the Shellshock issue.

Yet the next day, it was denied that it had been Shellshock that specifically had allowed these attacks.

  

* * *

### 🟡 Vulnerability:

Web servers are not the only vulnerable network resources. 

E-mail servers and DNS servers that use BASH to communicate with the OS could also be affected. 

While BASH is normally found on Unix-based systems, organizations using Windows-based systems are not immune. 

Those are probably leveraging appliances or hardware that are vulnerable.

Remember, BASH can be a part of home routers, many IoT devices and embedded systems. 
 
Shellshock can even be used to launch Denial of Service (DOS) attacks. 
 
Here is the line of code (a Bash function declaration followed by a semicolon and the ‘sleep’ command run from three possible paths to ensure it gets executed): new\_function() { :;} ; /bin/sleep 20 /sbin/sleep 20 | /usr/bin/sleep 20 This “sleep” command forces the server to wait twenty seconds before replying.

In doing so, resources on the machine are essentially held hostage because the machine can do nothing else for twenty seconds. One sleep command may be harmless, but an attacker may be able to replace this with malicious code.
 
Then, that code can handcuff the server or resource so it is unable to handle any requests. 
 
The risk of allowing harmful Internet users to execute commands of their choice remotely is high. 
 
By using the opening, bad actors may launch programs on the system, create outbound connections to their own systems and execute malicious software. 

Perhaps most critically, the vulnerability can be leveraged to steal confidential data and information stored on the system like credit card details, passwords and personally identifiable information (PII).

  

* * *

### 🟡 How to know that you are affected ?

Because Shellshock is six years old, plenty of vulnerability scanners are available. 

Some of them are free. One, bashcheck, can be downloaded using Github.

 For those technical people, typing a simple command in the Bash prompt will also do the trick: env X=”() { :;} ; echo Bash is Infected” /bin/sh -c “echo completed” env X=”() { :;} ; echo Bash is Infected” \`which bash\` -c “echo completed” env VAR='() { :;}; echo Bash is Infected‘ bash -c “echo completed” If the prompt returns a “Bash is Infected” message, it’s time to update and fix. 
 
If your output does not return “Bash is Infected,” it will respond with something like: bash: warning: VAR: ignoring function definition attempt bash: error importing function definition for \`VAR’ Bash Test If you’d like to test vulnerability for websites or specific CGI scripts, the following tool can help: ‘ShellShock’ Bash Vulnerability CVE-2014-6271 Test Tool. 

In either of the two input fields, enter the URL of the website or CGI script you’d like to test and click on the blue buttons.

  

* * *

### 🟡 How to be Protected ?

Most affected server and operating system providers have released software updates that debug the Shellshock vulnerability.

 There is a variety of mechanisms to check a system’s susceptibility or whether a patch has successfully resolved the problem. 
 
Log monitoring techniques should be used by organizations to detect any Shellshock exploitation; such a payload is delivered through a URL or HTTP header, hence it would leave evidence.

For securing an organization and successfully implementing effective vulnerability management the following points needs to be taken of:- Identifying vulnerability quickly: Speed is the key point. 

The systems should be monitored and scanned to check vulnerability threats. Adequate time and personnel should be deployed for thorough maintenance of system security. 

Determining the level of vulnerability: Knowing the organizations’ risk tolerance is essential in determining how severe a vulnerability might be. 

Depending on the network infrastructure, some vulnerabilities are more harmful than others. Mitigating the vulnerabilities: Update all firmware and operating system and install security updates. 

Use vulnerability detection tools or plug-ins to scan likely vulnerabilities. System administrators should patch systems immediately and closely track the network activity. 

Use the intrusion prevention system (ISP) when possible. 

Third-party vendor services: An organization that relies on third-party services should ensure that vendors take adequate security measures for the safety of their data. 

Caution: Caution needs to be taken particularly by Mac OS users. In the case of emails, any request for information or instructing to click a link or run software may often lead to phishing attacks.

  

* * *

### 🟡 Specific Exploitation Vectors

#### ⭐CGI-based web server :

When a web server uses the Common Gateway Interface (CGI) to handle a document request, it copies certain information from the request into the environment variable list and then delegates the request to a handler program. 

If the handler is a Bash script, or if it executes Bash, then Bash will receive the environment variables passed by the server and will process them as described above. 

This provides a means for an attacker to trigger the Shellshock vulnerability with a specially crafted document request. 

Security documentation for the widely used Apache web server states: "CGI scripts can ... be extremely dangerous if they are not carefully checked," and other methods of handling web server requests are typically used instead. 

There are a number of online services which attempt to test the vulnerability against web servers exposed to the Internet.

#### ⭐OpenSSH server :

OpenSSH has a "ForceCommand" feature, where a fixed command is executed when the user logs in, instead of just running an unrestricted command shell. 

The fixed command is executed even if the user specified that another command should be run; in that case the original command is put into the environment variable "SSH\_ORIGINAL\_COMMAND". 

When the forced command is run in a Bash shell (if the user's shell is set to Bash), the Bash shell will parse the SSH\_ORIGINAL\_COMMAND environment variable on start-up, and run the commands embedded in it.

 The user has used their restricted shell access to gain unrestricted shell access, using the Shellshock bug.

#### ⭐DHCP clients :

Some DHCP clients can also pass commands to Bash; a vulnerable system could be attacked when connecting to an open Wi-Fi network. 

A DHCP client typically requests and gets an IP address from a DHCP server, but it can also be provided a series of additional options. A malicious DHCP server could provide, in one of these options, a string crafted to execute code on a vulnerable workstation or laptop.

#### ⭐Qmail server :

When using Bash to process email messages (e.g. through .forward or qmail-alias piping), the qmail mail server passes external input through in a way that can exploit a vulnerable version of Bash.

#### ⭐IBM HMC restricted shell :

The bug can be exploited to gain access to Bash from the restricted shell of the IBM Hardware Management Console,a tiny Linux variant for system administrators. IBM released a patch to resolve this.

  

* * *

### 🟡 Conclusion:

While taking a tactical approach in order to eliminate the existing risk exposure caused by Shellshock, it is essential that all organizations take appropriate steps allowing them to detect, assess and protect themselves from future vulnerabilities by employing a vulnerability management framework tailored to their specific needs. 

Managing the emergence of new vulnerabilities is a key business process that underpins cyber security. 

Every organization should have the ability to identify vulnerabilities that impact them in a swift manner, rate their severity and take remedial action at an appropriate time. 

Typically, a mature organization would manage the resolution of a critical vulnerability posed by Shellshock or Heartbleed using the same measures they would employ for a serious security incident, in order to drive the urgency and visibility required.

  

BE ALERT ⚠️ BE SAFE
-------------------
