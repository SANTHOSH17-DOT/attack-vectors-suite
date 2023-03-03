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

    ![IDOR1](https://user-images.githubusercontent.com/125211284/222491379-596536ca-d18d-4c23-b49f-36523ca43b9c.png)

 #
 ## Simulation of IDOR

- I will try to simulate IDOR attack vector with the help of a lab. 
        
    Lab link : https://rb.gy/t7uykd

- After accessing the lab we will go to to "My Account" option as shown in the below image.

    ![2023-03-02 20_48_28-Insecure direct object references — Mozilla Firefox](https://user-images.githubusercontent.com/125211284/222491186-1c263b52-4623-4ad8-80c6-45841b419ebe.png)

- We will be shown a login page just like the one shown below
        
        The credentials are wiener:peter

    ![2](https://user-images.githubusercontent.com/125211284/222327896-f49c9645-5f7e-405e-b355-744eb7d33aa0.png)

- After logging in and clicking on "Live Chat" option on the top right corner, we see that there is a chatting feature.
- We can also download our older conversation. 

    ![2023-03-02 20_50_40-Insecure direct object references — Mozilla Firefox](https://user-images.githubusercontent.com/125211284/222491208-84c10d9e-fe7b-4ae8-89f9-d7555dc71a17.png)

- Before further steps we will start our "BurpSuite" and turn the intercept on and the browser's proxy.

    ![2023-03-01 20_12_00-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184331-6a306830-0a2b-4630-a92d-bd2e4160a530.png)

- After a little conversation if we try to do download our transcript by clicking on the "View Transcript" option, and we catch this request in the Burp.

    ![2023-03-02 21_18_35-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491224-b8b2450f-3647-47f6-a19a-a4852a8b2647.png)

- Here we can see all the conversation in the request, we just forward this request.

    ![2023-03-02 21_18_54-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491238-c967a850-96ca-42f3-a120-c24999e082e9.png)

- In the next request we see that, it is a request to download the chats, with the file name specified in the headers (here it is 6.txt).

    ![2023-03-02 21_20_15-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491263-ef60474c-0b76-48e7-b33e-148eb85a8d07.png)

- After requesting the previous request, we will see out file will be downloaded.

    ![2023-03-02 21_21_51-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491285-328d4652-df21-4e07-84c0-715dc31b0b89.png)

- Now we carry on the conversation and download the transcript again,

    ![2023-03-02 21_22_46-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491291-f66022e9-3a26-49bf-9314-539a832d8b2a.png)

- We now observe that the file name has increased by 1 (i.e. from 6.txt to 7.txt)

   ![2023-03-02 21_23_08-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491308-c4eb29b1-5bc2-48c8-b76b-894b450879d7.png) 

- Now we send this request to "Intruder" by clicking "Ctrl + I".
- And select the name of the file as our payload position, as shown below.

    ![2023-03-02 21_23_40-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491330-5c40fad4-2e80-4c68-a164-ba231ec99916.png)

- In the "payload" option we add few numbers, to see how many other files are present on the database and if we can access them.

    ![2023-03-02 21_24_16-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491338-350f4d4d-1a9d-499f-b3f9-6b9e9ec8a5cb.png)

- And the Burp result shows that there is a file "1.txt" too that is also present on the database (The files numbered from 2-7 are our chats only.)

    ![2023-03-02 21_25_25-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491343-c65c6ad3-3f40-4f94-b20a-e0f1c88d816c.png)

- Now we go back to "Proxy" tab and change the file name from 7.txt to 1.txt to download it (We have to do this for 2 requests one after the other)

    ![2023-03-02 21_32_37-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491355-620eca74-a4e0-4ff3-b0a3-431a34277680.png)

- And our file is downloaded.

    ![2023-03-02 21_33_39-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491367-b352d40d-2088-4a6e-8fde-7981dd7d1a53.png)

- Viewing the contents of the file we are able to steal a password, as shown below

    ![2023-03-02 21_35_10-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222491373-fb93bb1d-a635-4943-a2cc-164520fcbf5b.png)

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
