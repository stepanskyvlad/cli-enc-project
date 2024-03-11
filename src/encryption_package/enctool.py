"""
Enctool module. This module contains the main functions to encrypt and decrypt texts.

How to use the module:
1) Encrypt mode:
    1.1) python encytool.py --encrypt path/to/binary/key/file example_text.txt -
encrypts the text from example_text.txt using the binary key file and print the result on the console.

    1.2) python encytool.py --encrypt path/to/binary/key/file example_text.txt -w path/to/output/file -
encrypts the text from example_text.txt using the binary key file and write the result into the output file.

2) Decrypt mode:
    2.1) python encytool.py --decrypt path/to/binary/key/file example_text.txt -
decrypts the text from example_text.txt using the binary key file and return the result.

    2.2) python encytool.py --decrypt path/to/binary/key/file example_text.txt -w path/to/output/file -
decrypts the text from example_text.txt using the binary key file and write the result into the output file.
"""
from argparse import ArgumentParser, Namespace
import rsa
import sys
from utils import read_text_from_file, read_bytes_from_file, load_public_key, load_private_key


def encrypt_text(public_key: rsa.PublicKey, text: str) -> bytes:
    """
    Encrypt the text using the public key.

    Args:
        public_key (PublicKey): The public key.
        text (str): The text to be encrypted.

    Returns:
        bytes: The encrypted text.
    """
    encrypted_text = rsa.encrypt(text.encode("utf-8"), public_key)
    return encrypted_text


def decrypt_text(private_key: rsa.PrivateKey, encrypted_text: bytes) -> str:
    """
    Decrypt the text using the private key.

    Args:
        private_key (PrivateKey): The private key.
        encrypted_text (bytes): The encrypted text.

    Returns:
        str: The decrypted text.
    """
    decrypted_text = rsa.decrypt(encrypted_text, private_key).decode("utf-8")

    return decrypted_text


def write_encrypted_file(encrypted_text: bytes, file_path: str) -> None:
    """
    Write the encrypted text into a file.

    Args:
        encrypted_text (bytes): The encrypted text.
        file_path (str): The path to the file where the encrypted text will be written.

    Returns:
        None
    """
    with open(file_path, "wb") as f:
        f.write(encrypted_text)


def write_decrypted_file(decrypted_text: str, file_path: str) -> None:
    """
    Write the decrypted text into a file.

    Args:
        decrypted_text (str): The decrypted text.
        file_path (str): The path to the file where the decrypted text will be written.

    Returns:
        None
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(decrypted_text)


def parse_args(args) -> Namespace:
    """
    Parse the arguments.
    """
    parser = ArgumentParser(description='Encrypt or decrypt text using a binary key file.')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt mode')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt mode')
    parser.add_argument('key_file', type=str, help='Path to the binary key file')
    parser.add_argument('input_file', type=str, help='Path to the file to encrypt or decrypt')
    parser.add_argument('-w', '--write', type=str, help='Path to the file where the result will be written')

    return parser.parse_args(args)


def main():
    """
    Main function to run the module.
    """
    # Parse command-line arguments (excluding script name) using argparse
    args = parse_args(sys.argv[1:])
    # Encrypt mode
    if args.encrypt:
        public_key = load_public_key(args.key_file)
        text = read_text_from_file(args.input_file)
        encrypted_text = encrypt_text(public_key, text)
        # Write the encrypted text into a file or print it on the console
        if args.write:
            write_encrypted_file(encrypted_text, args.write)
            print(f"Text encrypted successfully. Encrypted text written into {args.write}")
        # Print the encrypted text on the console
        else:
            print(encrypted_text)

    # Decrypt mode
    elif args.decrypt:
        private_key = load_private_key(args.key_file)
        encrypted_text = read_bytes_from_file(args.input_file)
        decrypted_text = decrypt_text(private_key, encrypted_text)
        # Write the decrypted text into a file or print it on the console
        if args.write:
            write_decrypted_file(decrypted_text, args.write)
            print(f"Text decrypted successfully. Decrypted text written into {args.write}")
        # Print the decrypted text on the console
        else:
            print(decrypted_text)


if __name__ == "__main__":
    main()
