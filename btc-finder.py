import os
import hashlib
import base58
from tqdm import tqdm
from bitcoin import ecdsa_raw_sign, ecdsa_raw_recover, privtopub, pubtoaddr

# Function to generate private key
def generate_private_key():
    return os.urandom(32).hex()

# Function to convert private key to bitcoin address
def private_key_to_address(private_key):
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)
    return address

# Function to load addresses from text file
def load_addresses(file_path):
    with open(file_path, 'r') as f:
        addresses = set(line.strip() for line in f)
    return addresses

# Main function to generate and check addresses
def main():
    addresses = load_addresses('btc.txt')
    with tqdm(total=1000000, desc="Checking Addresses", unit="address") as pbar:
        while True:
            private_key = generate_private_key()
            address = private_key_to_address(private_key)
            
            if address in addresses:
                with open('found_addresses.txt', 'a') as f:
                    f.write(f'Address: {address}, Private Key: {private_key}\n')
                print(f'Found matching address: {address}, Private Key: {private_key}')
            
            pbar.update(1)

if __name__ == "__main__":
    main()
