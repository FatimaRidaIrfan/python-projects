from pathlib import Path

folder = Path(__file__).parent
file = open(folder / "sample.log", "r")

content = file.read()  
file.close()

info_count = 0 
warning_count = 0 
error_count = 0

for line in content.splitlines():
    if "INFO" in line:
        info_count += 1
    elif "WARNING" in line:
        warning_count += 1
    elif "ERROR" in line:
        error_count += 1

print("Info messages: " , info_count)
print("Warning messages: ", warning_count)
print("Error messages: ", error_count)