SETUID ATTACK
=============


### 🌟️ Introduction :

📌 Setuid (set user ID on execution) is a Unix file permission that allows users to run a program with elevated privileges.

📌 For example, the passwd command is owned by root and setuid, allowing users to change their password with temporary root access.
  

* * *

### 🌟️ File modes Viewing the setuid permission of a file :

🌟️ 📌 The setuid permission is indicated by an "s" in the "user execute" bit position when using the ls -l command to view a file's permissions. 

📌 E.g. ` ls -l /usr/bin/passwd `

* * *

### 🌟️ Setting the setuid permission of a file :

📌 To set setuid for an executable file, use chmod u+s myfile.

📌 Non-executable files with setuid have no effect, displayed as an uppercase "S" in ls -l myfile.
 
📌 To make it effective, add the user-executable permission u+x, which displays the setuid as a lowercase "s" in ls -l myfile."

* * *

### 🌟️ Setgid

📌 Setgid is set group ID on execution, the equivalent of setuid for groups. 

📌 It grants file permissions to the group owner, indicated by a lowercase "s" in the "group execute" position of ls -l. 

📌 An uppercase "S" means setgid is set but has no effect.

📌 Accessing a file with setgid is as if the user is a member of the owning group. 

📌 Setgid for a directory means new files created in it have the directory's group owner, and copied/moved files retain their original group ID.
* * *

### 🌟️ File modes

📌 Setuid and setgid are represented as 4 and 2 respectively in the high-order octal digit of a file's mode. 

📌 E.g. 6711 is setuid, setgid, and read/write/executable for owner, executable for group and others. 

📌 There's also a symbolic representation, e.g. u=rwx,go=x,ug+s. To modify an existing directory tree, use a command such as find /path/to/directory -type d -exec chmod g+s '{}' '\'

* * *

### 🌟️ Effects

📌 Setuid and setgid flags only have an effect on binary executable files and not on scripts, and their effect varies based on whether they're applied to files, directories, or non-binary executable files.

### 🌟️ When set on an executable file

📌 Setuid and setgid flags on executable files allow users to run programs with escalated privileges, either as the file owner (commonly root) or file's group. 

📌 This enhances security by allowing trusted programs to be run with restricted access.

📌 E.g. ping command with setuid flag grants users network privileges to execute even if they lack the required permission.

### 🌟️ Security impact

📌 Setuid and setgid flags raise security concerns when used improperly. 

📌 It's important to be careful when granting execution privileges to files. 

📌 Improper use can result in security risks as programs with raised privilege can't be altered by the user, but may still have vulnerabilities that can be exploited. 

📌 This is why setuid is ignored for shell scripts and why chroot system call is unavailable to non-root users on Unix. 

📌 To avoid potential security issues, always carefully design programs before setting setuid or setgid flags.

* * *

### 🌟️ When set on a directory

📌 Setgid on a directory causes files and subdirs created within to inherit its group ownership. 

📌 Directories and files already existing when setgid is applied are unaffected. 

📌 This allows for easier collaboration among a group of users without needing to set permissions for each file.

📌 The setuid permission set on a directory is ignored by most Unix/Linux systems. 

📌 However, FreeBSD can be configured to interpret setuid similarly to setgid, so files in the directory inherit the owner's user ID. 

📌 Most BSD-based systems have this behavior as default, but it's not necessary for them.
* * *

### 🌟️ Security

📌 Setuid/setgid bit on executables raises security concerns. 

📌 Developers must be careful in design and implementation to prevent vulnerabilities like buffer overruns and path injection. 

📌 An attacker exploiting a vulnerable setuid process running as root can execute arbitrary code with root privileges and compromise the system. 

📌 The process environment must also be properly sanitized to avoid exploitation through environment variables, as seen in past exploits like the one affecting GNU libc.
* * *

### 🌟️ Protecting setuid and setgid Programs

📌 Setuid programs allow a user to run a program with the permissions of its owner, usually root. 

📌 If the owner is root, the user executing the setuid program becomes a superuser with access to all system permissions.

📌 It's important to design setuid programs carefully to avoid security risks, including back doors and shells. 

📌 CA ControlMinder can be used to manage setuid and setgid programs, permitting only trusted programs to execute and protecting against unauthorized access.




