import hashlib

from pathlib import Path

folder = Path(__file__).parent 
file = open(folder / "sample.txt", "r" )

content = file.read()
file.close()

file_hash = hashlib.sha256(content.encode())

hash_value = file_hash.hexdigest()
original_hash = hash_value

input("Modify sample.txt if you want, then press enter to continue: ")

new_file = open(folder / "sample.txt", "r")
new_content = new_file.read()
new_file.close()

new_hash = hashlib.sha256(new_content.encode())
new_hash_value = new_hash.hexdigest()

if original_hash == new_hash_value:
    print("The file has not been modified.")
else:
    print("The file has been modified.")


print("SHA-256 Hash: ", hash_value)