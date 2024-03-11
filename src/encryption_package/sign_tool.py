"""
This module provides the sign tool. It can be used to sign a file or verify a signature file.
How to use the module:
1) Sign mode:
    python sign_tool.py -s path/to/key/file path/to/signature/file path/to/message/file
        - signs the message from the message file using the key file and saves the signature into the signature file.

2) Verify mode:
    python sign_tool.py -v path/to/key/file path/to/signature/file path/to/message/file
        - verifies the signature from the signature file using the key file and the message from the message file.
"""
import sys
import rsa
from utils import read_text_from_file, read_bytes_from_file, load_public_key, load_private_key
from argparse import ArgumentParser, Namespace


def sign_text(private_key: rsa.PrivateKey, text: str) -> bytes:
    """
    Sign the text using the private key.

    Args:
        private_key (PrivateKey): The private key.
        text (str): The text to be signed.

    Returns:
        bytes: The signature.
    """
    signature = rsa.sign(text.encode("utf-8"), private_key, "SHA-256")
    return signature


def verify_text(public_key: rsa.PublicKey, text: str, signature: bytes) -> bool:
    """
    Verify the signature of the text using the public key.

    Args:
        public_key (PublicKey): The public key.
        text (str): The text to be verified.
        signature (bytes): The signature to be verified.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    try:
        rsa.verify(text.encode("utf-8"), signature, public_key)
        return True
    except rsa.VerificationError:
        return False


def create_signature_file(signature: bytes, file_path: str) -> None:
    """
    Write the signature into a file.

    Args:
        signature (bytes): The signature.
        file_path (str): The path to the file where the signature will be written.

    Returns:
        None
    """
    with open(file_path, "wb") as f:
        f.write(signature)


def parse_args(args) -> Namespace:
    """Parse the arguments."""
    parser = ArgumentParser(description="Sign or verify a file.")
    parser.add_argument("-s", "--sign", action="store_true", help="Sign mode. Make a signature file")
    parser.add_argument("-v", "--verify", action="store_true", help="Verify mode. Verify a signature file")
    parser.add_argument("key_path", type=str, help="Path to the key file")
    parser.add_argument("signature_path", type=str, help="Path to the signature file")
    parser.add_argument("message_path", type=str, help="Path to the file with message.txt")

    return parser.parse_args(args)


def main():
    """Main function. Entry point of the program."""
    args = parse_args(sys.argv[1:])

    if args.sign:
        private_key = load_private_key(args.key_path)
        secret_message = read_text_from_file(args.message_path)
        signature = sign_text(private_key, secret_message)
        create_signature_file(signature, args.signature_path)
        print("Signature created successfully.")

    elif args.verify:
        public_key = load_public_key(args.key_path)
        secret_message = read_text_from_file(args.message_path)
        signature = read_bytes_from_file(args.signature_path)
        if verify_text(public_key, secret_message, signature):
            print("Signature is valid.")
        else:
            print("Signature is not valid.")


if __name__ == "__main__":
    main()
