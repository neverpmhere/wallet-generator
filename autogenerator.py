import secrets
from eth_keys import keys
from eth_utils import to_checksum_address

def generate_address_with_zeros():
    while True:
        private_key_bytes = secrets.token_bytes(32)
        private_key = keys.PrivateKey(private_key_bytes)
        address = private_key.public_key.to_checksum_address()
        if address.startswith("0x00000") and address.endswith(""):
            return private_key, address
        else:
            return 0
    
while True:
    found = False
    print("No addresses with leading zeros found.")
    with open("found_addresses.txt", "a") as file:
        for i in range(0, 10):
            address = generate_address_with_zeros()
            if address:
                found = True
                print("Private Key:", address[0])
                print("Address:", address[1])
                file.write(str(address[0]) + " " + str(address[1]) + "\n")             