#!/usr/bin/python2
# -*- coding: utf-8 -*-

import json
import socket
import sys

def main():
    try:
        title = sys.argv[1]
        body = sys.argv[2]
    except IndexError:
        print "Too few arguments. kthxbai."
        sys.exit(0)

    message = {
        'title': title,
        'body': body
    }

    send_message(message)


def send_message(message_dict):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 12345))
    s.send(json.dumps(message_dict))
    s.close()


if __name__ == "__main__":
    main()
