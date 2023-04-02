Cross-Site Scripting (XSS)
=========================

## What is Cross-Site Scripting ??

- Cross-site scripting attacks, also called XSS attacks, are a type of injection attack that injects malicious code into otherwise safe websites.

- An attacker will use a flaw in a target web application to send some kind of malicious code, most commonly client-side JavaScript, to an end user. Rather than targeting the application’s host itself, XSS attacks generally target the application’s users directly.

- The actual attack occurs when the victim visits the web page or web application that executes the malicious code. 

- The web page or web application becomes a vehicle to deliver the malicious script to the user’s browser.


## Types of XSS


 There are three main types of XSS attacks. These are:

    - Reflected XSS
    - Stored XSS
    - DOM-based XSS


## Cross-site Scripting Attack Vectors

- The following is a list of some of the XSS attack vectors that an attacker could use to compromise the security of a website or web application through an XSS attack:
       
       - <script> tag
       - <img> tag
       - <iframe> tag
       - <svg> tag
       - <body> tag
       - <input> tag
       - <table> tag
       - JavaScript events



## Simulation of XSS 

- I will try to simulate a XSS attack with the help of a lab and will show how to use some of the above mentioned attack vectors in practice.

  Lab link : https://rb.gy/wwmjho


- The lab is a blog website with a XSS prone Search Bar. (All these are examples of Reflected XSS )


### \<script> tag

- The \<script> tag is the most straightforward XSS payload.

- A script tag can reference external JavaScript code or you can embed the code within the script tag itself.

         The Javascript code used here is <script>alert(1)</script>


![WhatsApp Image 2023-02-25 at 10 13 12 PM (1)](https://user-images.githubusercontent.com/77486870/221369216-68f896b5-6c40-47cd-8648-588cb4c8fd02.jpeg)
 
![WhatsApp Image 2023-02-25 at 10 13 12 PM](https://user-images.githubusercontent.com/77486870/221369163-d66cb100-a151-48cc-bb01-a5fc0cd73417.jpeg)

### \<iframe> tag

- The \<iframe> tag lets you embed another HTML page in the current page. 

- IFrames are still very effective for pulling off phishing attacks.

        The Javascript code used here is <iframe src="" onload=alert(0)>

![WhatsApp Image 2023-02-25 at 10 13 13 PM (3)](https://user-images.githubusercontent.com/77486870/221369400-53f7df2f-8243-400b-9894-fcc140145139.jpeg)

![WhatsApp Image 2023-02-25 at 10 13 13 PM (2)](https://user-images.githubusercontent.com/77486870/221369351-e77dfe07-e62a-42a3-94b9-4678364b3e53.jpeg)

### \<img> tag

- Some browsers execute JavaScript found in the \<img> attributes.

        The Javascript code used here is <img src="" onerror=alert(1)>

![WhatsApp Image 2023-02-25 at 10 13 13 PM (5)](https://user-images.githubusercontent.com/77486870/221369463-b899efcd-2702-429f-9104-c3daeaff2a89.jpeg)

![WhatsApp Image 2023-02-25 at 10 13 13 PM (4)](https://user-images.githubusercontent.com/77486870/221369434-c99be652-362e-4257-963d-db5dfbde407c.jpeg)

### \<svg> tag

- Just like \<img> tag we can also use \<svg> tag in order to execute a XSS attack.

        The Javascript code used here is <svg src="" onload=alert(1)>

![WhatsApp Image 2023-02-25 at 10 13 13 PM (1)](https://user-images.githubusercontent.com/77486870/221369329-bb767070-b258-4a5d-a908-0aeb298ff5ad.jpeg)

![WhatsApp Image 2023-02-25 at 10 13 13 PM](https://user-images.githubusercontent.com/77486870/221369271-78be6538-6925-4ac3-bba5-80a8c973a567.jpeg)

### JavaScript events

- JavaScript event attributes such as onload and onerror etc. can be used in many different tags. 

- This is a very popular XSS attack vector.

        The Javascript code used here is "onmouseover="alert(1)


![WhatsApp Image 2023-02-25 at 10 13 13 PM (7)](https://user-images.githubusercontent.com/77486870/221369536-e2710336-deaf-4612-9143-3bd6d5effe66.jpeg)

![WhatsApp Image 2023-02-25 at 10 13 13 PM (6)](https://user-images.githubusercontent.com/77486870/221369494-27de0365-a788-443d-8884-90ec821cfb46.jpeg)


