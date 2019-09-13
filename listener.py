#!/usr/bin/python 3
import socket


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.75.131", 4444))
listener.listen(0)
print("[+] Waiting for incoming connections")
listener.accept()
print("[+] Got a connection")

