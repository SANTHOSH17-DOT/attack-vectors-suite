Insecure Direct Object Reference
================================

## What is Insecure Direct Object Reference (IDOR)??

- In IDOR vulnerabilities, an attacker can manipulate the application to gain access to internal objects, such as files or database records, which they should not 
have access to.

- This is possible when the application exposes a reference to an internal object without proper access controls, allowing the attacker to bypass authorization checks and access the object directly.

- This can allow attackers to bypass access controls and view or modify sensitive data that they should not have access to.

### Example of IDOR

 - Consider a web application that allows users to view their own account information by providing an account ID. 
 
 - If the application does not properly validate that the account ID belongs to the currently authenticated user, an attacker could simply modify the ID in the request to view another user's account information.

 #
 ## Simulation of IDOR

- I will try to simulate IDOR attack vector with the help of a lab. 
        
    Lab link : https://rb.gy/t7uykd

- After accessing the lab we will go to to "My Account" option as shown in the below image.


- We will be shown a login page just like the one shown below
        
        The credentials are wiener:peter

    ![2](https://user-images.githubusercontent.com/125211284/222327896-f49c9645-5f7e-405e-b355-744eb7d33aa0.png)

- After logging in and clicking on "Live Chat" option on the top right corner, we see that there is a chatting feature.
- We can also download our older conversation. 

- Before further steps we will start our "BurpSuite" and turn the intercept on and the browser's proxy.

 ![2023-03-01 20_12_00-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184331-6a306830-0a2b-4630-a92d-bd2e4160a530.png)

- After a little conversation if we try to do download our transcript by clicking on the "View Transcript" option, and we catch this request in the Burp.


- Here we can see all the conversation in the request, we just forward this request.


- In the next request we see that, it is a request to download the chats, with the file name specified in the headers (here it is 6.txt).


- After requesting the previous request, we will see out file will be downloaded.


- Now we carry on the conversation and download the transcript again,

- We now observe that the file name has increased by 1 (i.e. from 6.txt to 7.txt)

- Now we send this request to "Intruder" by clicking "Ctrl + I".
- And select the name of the file as our payload position, as shown below.

- In the "payload" option we add few numbers, to see how many other files are present on the database and if we can access them.


- And the Burp result shows that there is a file "1.txt" too that is also present on the database (The files numbered from 2-7 are our chats only.)


- Now we go back to "Proxy" tab and change the file name from 7.txt to 1.txt to download it (We have to do this for 2 requests one after the other)


- And our file is downloaded.

- Viewing the contents of the file we are able to steal a password, as shown below

#
## Impacts of IDOR

Impacts of IDOR Vulnerability:

- Exposure of Confidential Information: 
    - When the attacker will have control over your account via this vulnerability, it is obvious that an attacker will be able to come across your personal information.
- Authentication Bypass: 
    - As the attacker can have access to millions of accounts with this vulnerability, it will be a type of Authentication bypass mechanism.
- Alteration of Data: 
    - An attacker may have privileges to access your data and alter it. By this, an attacker may have permission to make changes to your data, which may lead to the manipulation of records.
- Account Takeover: 
    - While an attacker may have multiple access to user accounts just by changing the “UID” values, this will lead to account takeover vulnerability. When one vulnerability leads to another vulnerability(like in this case), It is known as the Chaining of BUGS.
#

## How to prevent IDOR??

To prevent IDOR attacks, there are several measures you can take:
    
    - Implement access controls
    - Use indirect references
    - Validate input
    - Use secure coding practices 
    - Perform regular security testing