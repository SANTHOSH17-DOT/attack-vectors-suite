# SQL Injections

By taking advantage of programme flaws, SQL Injection attacks (also known as SQLi) change SQL queries and inject malicious code.


SQL Injection is a vulnerability where an application takes input from a user and doesn't vaildate that the user's input doesn't contain additional SQL


## Impacts

- Steal credentials - Through SQLi, attackers can gain credentials, which they can then use to pose as users and access resources.
- Access databases - Attackers can access the private information stored on database servers.
- Delete data: Attackers are able to dump entire tables or delete database records.


![image](https://user-images.githubusercontent.com/83408515/199063080-b4d3492b-9a86-489c-9190-8454ffe38684.png)

![WhatsApp Image 2022-10-31 at 22 02 35](https://user-images.githubusercontent.com/83408515/199063152-990d61f0-721a-4988-a79f-c17498518dee.jpeg)tment 

So this can excute statement by statement and drops the database in the second statement if following is passed in the input box

![image](https://user-images.githubusercontent.com/83408515/199066647-bc7cc8d9-b801-41ac-ab99-31698dd9f3d1.png)


This can be more clearly understood by taking an example of a SQL injection challenge from a CTF contest .
Here this is the web page that is connected to the backend database to fetch the user records .

![imagea][def]




[def]:~/attack-vectors-suite/assets/html-sql-injection.png