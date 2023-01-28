# SQL Injections

### By taking advantage of programme flaws, SQL Injection attacks (also known as SQLi) change SQL queries and inject malicious code.


### SQLi is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to retrieve. An SQLi involves giving input to the SQL query that is not simply data, but an SQL query in itself. 

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

Now to exploit this , a clever person can use some SQL query instead of a normal answer and one potential way could be by using '1'='1' argument in the

query , it is shown below 

#### ( note that the default user input is taken in string fashion that is if xxxx is input the query takes it as 'xxxx' )
So if one gives the input as hello' or '1' = '1 to the query it looks like

''' 'hello' or '1' = '1' and as the or condition of '1'='1'  '''  is always **true** .

![imageb][defb]


#### Hence the  query renders all the information of trhe database and hence we are successful in exploiting it :) 

![imagec][defc]




[def]:https://github.com/bhumirao/attack-vectors-suite/blob/main/assets/html-sql-injection.png

[defb]:https://github.com/bhumirao/attack-vectors-suite/blob/main/assets/sql-2.png

[defc]:https://github.com/bhumirao/attack-vectors-suite/blob/main/assets/sql-3.png
