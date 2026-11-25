import platform
import socket 
import sys
import getpass

print("==== System Information ====\n")

print(f"Hostname: {socket.gethostname()}")
print(f"Python Version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} ")
print(f"Current user: {getpass.getuser()}")

print(f"Operating System: {platform.system()}")
print(f"OS Release: {platform.release()}")
print(f"Machine Architecture: {platform.machine()}")
print(f"Processor: {platform.processor()}")

print("==========================")