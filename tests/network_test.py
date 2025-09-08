# tests/network_test.py

import socket, time

def check_outbound():
    s = socket.socket()
    s.settimeout(3.0)
    try:
        s.connect(("1.1.1.1", 80))
        s.close()
        return True
    except Exception:
        return False

if not check_outbound():
    print("No outbound network access detected. Good.")
else:
    print("Outbound access available. Please apply firewall or disable NIC.")
