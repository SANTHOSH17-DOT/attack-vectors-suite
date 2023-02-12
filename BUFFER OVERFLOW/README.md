Buffer Overflow
===============

### 👉 What is Buffer Overflow ?

📌 A buffer overflow occurs when a program writes more data to a memory buffer than its capacity, leading to the overwriting of adjacent memory. 

📌 This can be prevented by adding bounds checks to flag or discard excess data.

  

* * *

### 👉 What is Buffer Overflow Attack

📌 A buffer overflow attack occurs when a program is forced to store more data than its buffer can hold. 

📌 This leads to the attacker being able to overwrite memory, change the execution path of the program, and gain access to sensitive information or systems. 

📌 Attackers may also feed input that causes a buffer overflow and replace areas of executable code with their own code, giving them control over the program.


### 👉Types of Buffer Overflow Attacks

📌 Stack & Heap-based buffer overflows: Stack-based buffer overflows are more common & occur when a program writes more data to the stack memory than it can handle.

📌 Heap-based buffer overflows are harder & occur when a program writes more data to the heap memory than it can handle. 

📌 Both can lead to memory overwrites & damaging program execution.

  

* * *

### 👉 What Programming Languages are More Vulnerable?

📌 C and C++ are prone to buffer overflow attacks due to lack of built-in safeguards for memory access and overwrite. 

📌 Many operating systems like Windows, Linux and Mac OSX use C and C++ code.

📌 Languages with safety mechanisms like Java, PERL, JavaScript and C# have reduced likelihood of buffer overflows.

  

* * *


### 👉 How to Prevent Buffer Overflows ?

📌 Developers can prevent buffer overflow attacks by using secure coding practices, such as bounds checking and proper memory allocation, or by programming in languages that have built-in safeguards. 

📌 Operating systems also have security features, such as runtime protection, to prevent buffer overflows.

Three common protections are :

📌 Protection against buffer overflow attacks includes address space randomization, data execution prevention, and structured exception handler overwrite protection. 

📌 ASLR randomizes data regions, making it difficult for attackers to locate code. 

📌 Data execution prevention marks memory regions as non-executable to prevent code execution.

📌 SEHOP protects against exploitation of structured exception handling, a system for managing hardware and software exceptions
  

* * *

### 👉 Key Concepts of Buffer Overflow

📌 A buffer overflow error happens when data exceeds the buffer capacity, leading to adjacent storage overwriting. 

📌 This can result in system crashes or be exploited by cyberattacks.

📌 Secure development includes regular testing and using language-level protection and run-time bounds-checking.

  

* * *

### 👉 Buffer Overflow Solutions

📌 To prevent buffer overflows, use secure coding practices such as avoiding functions that lack bounds checking, regular testing, and automatic protection at the language level. 

📌 Bounds checking at runtime can also help prevent buffer overrun by ensuring that data written to a buffer is within acceptable limits.


* * *

### 👉 Important Keyword and Info 

📌 ASLR - "Address space layout randomization"

📌 PERL - "Practical Extraction and Reporting Language used for system administration, networking, and other applications that involve user interfaces"

📌 SEHOP - "SEHOP is a exploit protection feature of Windows 10 that helps prevent malicious code from attacking Structured Exception Handling"

📌 One of the most famous attacks of buffer overflow are [SQL Slammer](https://en.wikipedia.org/wiki/SQL_Slammer) and [The Morris Worm](https://en.wikipedia.org/wiki/Morris_worm)🧐