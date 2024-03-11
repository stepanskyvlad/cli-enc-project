"""
This module contains utility functions for the encryption package.
"""
import rsa
from typing import List


def read_text_from_file(folder_path: str) -> str:
    """
    Read lines of files from a folder and return them as a list of strings.

    Args:
        folder_path (str): The path to the folder of the files to be read.
    Returns:
        List[str]: A list containing each line of the file as a string.

    Raises:
        FileNotFoundError: If the specified file is not found.
        PermissionError: If there is a permission error while trying to open the file.
    """
    try:
        with open(folder_path, "r", encoding="utf-8") as f:
            text = "".join(f.readlines())
        return text
    except (FileNotFoundError, PermissionError) as e:
        raise FileNotFoundError(f"Error reading file: {e}")


def read_bytes_from_file(folder_path: str) -> bytes:
    """
    Read the bytes from a file.

    Args:
        folder_path (str): The path to the file to be read.

    Returns:
        bytes: The bytes read from the file.

    Raises:
        FileNotFoundError: If the specified file is not found.
        PermissionError: If there is a permission error while trying to open the file.
    """
    try:
        with open(folder_path, "rb") as f:
            return f.read()
    except (FileNotFoundError, PermissionError) as e:
        raise FileNotFoundError(f"Error reading file: {e}")


def load_public_key(key_path: str) -> rsa.PublicKey:
    """
    Load the public key from the file.

    Args:
        key_path (str): The path to the file containing the public key.

    Returns:
        PublicKey: The public key.
    """
    with open(key_path, "rb") as f:
        return rsa.PublicKey.load_pkcs1(f.read())


def load_private_key(key_path: str) -> rsa.PrivateKey:
    """
    Load the private key from the file.

    Args:
        key_path (str): The path to the file containing the private key.

    Returns:
        PrivateKey: The private key.
    """
    with open(key_path, "rb") as f:
        return rsa.PrivateKey.load_pkcs1(f.read())
