"""
This module is responsible for generating a pair of public and private keys and saving them into a folder.
How to use it:
1) python generate_keys.py path/to/folder
    - generates a pair of public and private keys and saves them into the folder
"""
import rsa
from argparse import ArgumentParser, Namespace
import os
import sys
from typing import Tuple


def generate_key_pair(bits=1024) -> Tuple[bytes, bytes]:
    """
    Generate a pair of public and private keys.

    Args:
        bits (int): The number of bits to be used in the key.

    Returns:
        tuple: A tuple containing the public and private keys.
    """
    public_key, private_key = rsa.newkeys(bits)
    return public_key.save_pkcs1("PEM"), private_key.save_pkcs1("PEM")


def save_key(key, folder_path) -> None:
    """
    Save the key into the folder.

    Args:
        key (bytes): The key to be saved.
        folder_path (str): The path to the folder where the key will be saved.
    """
    with open(folder_path, "wb") as f:
        f.write(key)


def parse_args(args) -> Namespace:
    """Parse the arguments."""
    parser = ArgumentParser(description="Create and save public and private keys into the folder")
    parser.add_argument("keys_folder", type=str, help="Path to the folder")

    return parser.parse_args(args)


def main():
    """Main function. Entry point of the program."""
    # Parse command-line arguments (excluding script name) using argparse
    args = parse_args(sys.argv[1:])
    # Generate keys
    public_key, private_key = generate_key_pair()
    # Save public key
    save_key(key=public_key, folder_path=os.path.join(args.keys_folder, "public.pem"))
    # Save private key
    save_key(key=private_key, folder_path=os.path.join(args.keys_folder, "private.pem"))
    print("RSA key pair generated and saved successfully. Keys are saved in the folder: ", args.keys_folder)


if __name__ == "__main__":
    main()
