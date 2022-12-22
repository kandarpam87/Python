#!/bin/python
import socket

cronet_restricted_ports = [
    1, 7, 9, 11, 13, 15, 17, 19, 20, 21, 22, 23, 25, 37, 42, 43, 53, 77, 79, 87,
    95, 101, 102, 103, 104, 109, 110, 111, 113, 115, 117, 119, 123, 135, 139,
    143, 179, 389, 465, 512, 513, 514, 515, 526, 530, 531, 532, 540, 556, 563,
    587, 601, 636, 993, 995, 2049, 3659, 4045, 6000, 6665, 6666, 6667, 6668,
    6669, 6697
]

chk = [
        port for port in range(1025, 32766)
        if port not in cronet_restricted_ports
    ]

def can_connect(port):
    # this test is only really useful on unices where SO_REUSE_PORT is available
    # so on Windows, where this test is expensive, skip it
    if platform.system() == 'Windows': return False
    s = socket.socket()
    try:
        s.connect(('localhost', port))
        return True
    except socket.error as e:
        return False
    finally:
        s.close()


def can_bind(port, proto):
    s = socket.socket(proto, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind(('localhost', port))
        return True
    except socket.error as e:
        return False
    finally:
        s.close()


for i in chk:
    if can_bind(i, socket.AF_INET) and can_bind(
            i, socket.AF_INET6) and not can_connect(i):
        print("Port ", i, " is avaliable")
    else:
        print("Port ", i, " is not avaliable")
	