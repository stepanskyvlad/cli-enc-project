# CLI encryption package

This package is a simple command line interface for encrypting and
decrypting files using the RSA encryption algorithm.

## Modules
There are three modules in this package:
### 1. generate_keys module
### 2. enctool module
### 3. signtool module

## How to use:

### 1. generate_keys module
This module is used to generate a pair of RSA keys. The keys are saved 
in the given directory as `private.pem` and `public.pem`.

#### Usage:
>[!IMPORTANT]
>The directory must exist before running the module.
> You mustn't give the names of the key files.
> The module will name `private.pem` and `public.pem` automatically
> in the provided directory.
> The module will overwrite the existing keys in the directory.

```commandline
py generate_keys.py path/to/directory
```

#### Example:
```commandline
py src\encryption_package\generate_keys.py keys
```

### 2. enctool module
This module is used to encrypt and decrypt files using the RSA algorithm.
The module uses the private and public keys. If you don't have such keys,
you can generate them by the `generate_keys` module.

#### Usage:
>[!IMPORTANT]
> The directories must exist before running the module.
> The module will overwrite the existing files in the directory.

#### 1) Encrypt mode:
#### 1.1) Encrypt and print the result on the console:
```commandline
py encytool.py --encrypt path/to/binary/key/file path/to/input/file
```
#### Example:
```commandline
py src\encryption_package\enctool.py --encrypt keys\public.pem files\example_text.txt
```

#### 1.2) Encrypt and write the result into the output file:
```commandline
py encytool.py --encrypt path/to/binary/key/file path/to/input/file -w path/to/output/file
```

#### Example:
```commandline
py src\encryption_package\enctool.py --encrypt keys\public.pem files\example_text.txt -w files\encrypted_text
```

#### 2) Decrypt mode:
#### 2.1) Decrypt and print the result on the console:
```commandline
py encytool.py --decrypt path/to/binary/key/file path/to/encrypted/file
```

#### Example:
```commandline
py src\encryption_package\enctool.py --decrypt keys\private.pem files\encrypted_text 
```

#### 2.2) Decrypt and write the result into the output file:
```commandline
py encytool.py --decrypt path/to/binary/key/file path/to/encrypted/file -w path/to/output/file
```

#### Example:
```commandline
py src\encryption_package\enctool.py --decrypt keys\private.pem files\encrypted_text -w files\decrypted_file.txt
```

### 3. signtool module
This module is used to sign and verify files using the RSA algorithm.
The module uses the private and public keys. If you don't have such keys,
you can generate them by the `generate_keys` module.

#### Usage:
>[!IMPORTANT]
> The directories must exist before running the module. 
> The module will overwrite the existing files in the directory.

#### 1) Sign mode:
Signs the message from the message file using the key file and saves the signature into the signature file.
```commandline
py signtool.py --sign path/to/key/file path/to/signature/file path/to/message/file
```

#### Example:
```commandline
py src\encryption_package\signtool.py --sign keys\private.pem files\signature files\example_text.txt 
```

#### 2) Verify mode:
Verifies the signature from the signature file using the key file and the message from the message file.
```commandline
py signtool.py --verify path/to/key/file path/to/signature/file path/to/message/file
```

#### Example:
```commandline
py src\encryption_package\signtool.py --verify keys\public.pem files\signature files\example_text.txt
```

## Author
- Vladyslav Yarema

## License
- This project is licensed under the MIT License.