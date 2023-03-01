FILE UPLOAD VULNERABILITY
=========================

## What is File Upload Vulnerability ??

- File upload vulnerabilities are a type of security vulnerability that allows an attacker to upload a malicious file to a web server or application, potentially  allowing them to execute arbitrary code or gain unauthorized access to sensitive data.
- File uploads without restrictions can result in system/server takeover, overload file systems and databases, forwarding attacks to back-end systems, or even defacements. 
- This depends on how the application deals with the uploaded files and where the files are stored.

## Some important points about file upload vulnerabilities:
#
### How file upload vulnerabilities work:

- A file upload vulnerability can occur when an application or website allows users to upload files without proper validation of file type, size, and content. 
- Attackers can exploit this by uploading malicious files (such as PHP shells, backdoors, or viruses) that can be executed on the server, allowing them to gain unauthorized access to sensitive data, modify website content, or launch attacks against other users.

### Common causes of file upload vulnerabilities:

- Lack of file type validation: not checking if uploaded files are of the expected type.

- Lack of file size validation: allowing files that are too large, which can cause server crashes or buffer overflows.

- Lack of content validation: not checking the contents of the uploaded files for malicious code or scripts.

- Incorrect file permissions: allowing uploaded files to be executed as scripts or to overwrite existing files.

## Simulation of File Upload Vulnerability: 
#

- I will try to simulate a File upload vulnerability attack with the help of a lab.

- The lab contains a vulnerable image upload function and it doesn't perform any validation on the files users upload before storing them on the server's filesystem. 

#
### CASE 1: When there is no restiction on extension of file
Lab link : https://rb.gy/h1ayt6

After accessing the lab we will go to to "My Account" option as shown in the below image.

We will be shown a login page just like this one

    The credentials are wiener:peter

As we can see, we have an option to upload a file to updae our profile picture.
We will try to exploit this feature.

Now we upload a file named shell2.php (a webshell to access the command prompt of the target server).

And we see that our shell is successfully uploaded

After clicking "Back to my account" option, we see our profile picture icon has changed
Now we right click on the image and click on the option "Open Image in New Tab".

Now we go to the new tab in which our image is opened.

We now add
        
    ?cmd=
in the url, just as shown in the picture

The URL will now work as any other command prompt and we can use it to run any command like "ls" (to list the files and folders in the current directory)

As the task of this lab is to read a file "secret" in the home directory of "carlos", therefore we use the command:

    cat /home/carlos/secret

And we successfully got the flag

#
### CASE 2: When there are some restrictions on extension of file
Lab link : https://rb.gy/eujf9q

In this example some of the extensions are restricted by the website.
So we will try to bypass these restrictions

In this example when we try to upload our "shell2.php" file, we see an error message saying that php files are not allowed.

Now to tacle this problem, we take help of "BurpSuite"
Therefore we start BurpSuite and select the option "Intercept is on"

Now after turning on the proxy we will again try to upload our webshell.
This time we will see that our request is intercepted by BurpSuite.
We will now send this request to the "Intruder" by pressing "Ctrl + I" keys.

In the Intruder tab we select the extension of the file (here it is php) and add as a payload position.

Now in the payload tab we will add some of the other extensions used by php webshells.
Here I used

    php
    php3
    php4
    php5
    phtml

And we hit "Start Attack" option

Now in the results we can see that the extensions

    php3
    php4
    php5

got a "200" as a status i.e. they are not the restricted extensions

Now we go back to our "Proxy" tab and change the extension of our file from ".php" to ".php5" and forward the request.

And we will see that our shell is successfully uploaded.


    So like this we can exploit a simple feature of file upload and can gain control over the whole system.
#
## How to prevent file upload vulnerabilities??

The most effective way to protect your own websites from these vulnerabilities is to implement all of the following practices: 

- Check the file extension against a whitelist of permitted extensions rather than a blacklist of prohibited ones. It's much easier to guess which extensions you might want to allow than it is to guess which ones an attacker might try to upload.
- Make sure the filename doesn't contain any substrings that may be interpreted as a directory or a traversal sequence (../).
- Rename uploaded files to avoid collisions that may cause existing files to be overwritten.
- Do not upload files to the server's permanent filesystem until they have been fully validated. 

![2023-03-01 18_05_14-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184145-f93c1d79-e9af-4c5c-b7d7-c1d241634933.png)
![2023-03-01 18_06_24-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184157-b3ae82a8-9ca1-4123-84d5-cabf3e8974ad.png)
![2023-03-01 18_33_37-NVIDIA GeForce Overlay](https://user-images.githubusercontent.com/125211284/222184167-93e56efe-6406-498c-b469-db862ec5ced3.png)
![2023-03-01 18_36_54-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184207-9ca2e829-28fd-4895-9e1c-26b32c0a23fa.png)
![2023-03-01 18_37_45-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184218-35970fed-6c95-4f82-83a7-30498a4a8925.png)
![2023-03-01 18_38_18-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184236-e3773292-d6f4-475d-8a5d-4f292c357805.png)
![2023-03-01 18_38_36-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184247-ce4d1f36-a0ba-4a08-b545-df613a1c8c46.png)
![2023-03-01 18_39_01-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184254-71d610f6-7f64-49b2-a19e-7704312c89fe.png)
![2023-03-01 18_40_19-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184283-dad7805d-2343-47c3-a9c2-e6cbb246f53b.png)
![2023-03-01 18_41_01-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184299-a84a73a4-742a-4fdb-af36-26e48234046d.png)
![2023-03-01 20_11_08-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184313-e0c41936-41df-476a-8b5c-c617cef30d7e.png)
![2023-03-01 20_11_30-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184321-aaf9b835-7ab7-4c26-aa1f-0064846ea8c4.png)
![2023-03-01 20_12_00-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184331-6a306830-0a2b-4630-a92d-bd2e4160a530.png)
![2023-03-01 20_13_08-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184340-2baf508a-7c46-48a4-8759-e5018cf280e2.png)
![2023-03-01 20_13_41-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184350-1291abe8-6d70-4de3-91a6-c79f212e1d67.png)
![2023-03-01 20_14_40-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184356-d147d244-e310-4b94-9743-ca22fc1e30d3.png)
![2023-03-01 20_15_25-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184377-9552e8cc-09e4-4597-bd22-201d688e956c.png)
![2023-03-01 20_15_52-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184384-365062c9-623a-4413-83d0-e5f7ba111f96.png)
![2023-03-01 20_16_36-Kali  Running  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/125211284/222184390-c5290349-b300-48d7-b509-d035b7d208a4.png)




