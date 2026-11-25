import socket

target_ips = ["127.0.0.1"]

ports = [22, 80, 443, 8080]


def scan_port(target_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((target_ip, port))
        print(f"The port is reachable. IP Address: {target_ip} Port: {port}")
    except ConnectionRefusedError:
        print("The target port refused the connection.")
    except socket.timeout:
        print("Connection timed out.")
    finally:
        s.close()

for target_ip in target_ips:
    for port in ports:
        print("Checking port: ", port)
        scan_port(target_ip, port)
         