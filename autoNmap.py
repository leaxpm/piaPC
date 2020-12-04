import logging
try:
    import nmap
except:
    logging.error("Falta la libreria nmap \n pip install python-nmap")
import requests
import socket

def publicIP():
    """
        **PublicIP**
        This Module find the public IP from the User
    """
    req = requests.get("http://ifconfig.me")
    return req.text

def scanner(ip):
    """
        **Scanner**
        This Module Scan a given IP for ports 1-1000
    """
    scanner = nmap.PortScanner()
    out = scanner.scan(ip,"1/1000")
    return out

def privIp(): #Github Phanthaihuan
    """
        **PrivIP**
        This Module find the private IP from the User
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    out = (s.getsockname()[0])
    s.close()
    return out

def exec(scan):
    if scan == "private":
        segmento = ".".join(privIp().split('.')[0:3])+".0/24"
        return scanner(segmento)
    elif scan == "public":
        return scanner(publicIP())
