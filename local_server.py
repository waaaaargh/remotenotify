#!/usr/bin/python2
# -*- coding: utf-8 -*-

import socket
import subprocess
import pynotify
import json

# config
global identity
identity = "johannes@weltraumpflege.org"
port = 12345



def main():
    pynotify.init("SSH Remote")


    # establish ssh connection
    autossh_process = subprocess.Popen(["autossh", identity,  "-M 20000",
                                        "-R %i:localhost:%i" % (port, port),
                                        "-N", "-o ServerAliveInterval=5"])

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("localhost", 12345))
    serversocket.listen(5)

    try:
        while True:
            conn, addr = serversocket.accept()
            data = conn.recv(1024)

            message_dict = json.loads(data)
            notification = pynotify.Notification(message_dict['title'], message_dict['body'])
            notification.show()

    except KeyboardInterrupt:
        autossh_process.kill()
        serversocket.close()

if __name__ == "__main__":
    main()
