remotenotify
============

Display notifications on your desktop from your VPS or Home Server and continue after loss of network connection / suspend.

## Usage
1. Configure your SSH Server and client to authenticate via public key rather than password.
2. Satisfy dependecies.
     * autossh
     * pynotify
3. Edit the ```local_server.py``` script to match your identity for the ssh login and a free port.
4. run ```local_server.py```
5. setup your applications to call ```remote_notify.py``` for notifications
6. enjoy!

## Security implications
**Warning:** remotenotify dedicates a specific port to forwarding notifications. That means: you either should be the only one to use the server or be on really good terms with the users. Any port number larger than 1024 can be allocated even by unprivileged users, that means that they can in fact read your messages. Anyways, every user on the system can connect to any port on the system, that means that either way, they can send you bogus notifications. As remotenotify only opens ports on the loopback interface of the remote server, noone but users with accounts on the remote server can access this ports, so you are fine, if you are the only one with an account on this server.
