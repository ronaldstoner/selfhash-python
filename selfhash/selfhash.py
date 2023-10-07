#!/usr/bin/python
# Hash: 84e58a4a1dbd6cdae11fd89f7a718154ab7a1e140dc2860c4428aa4d87789010

# No password is set for this hash as it is used to verify the selfhash module code itself and can be checked against the github repo

"""SelfHash - Self hashing and verification python script"""

import hashlib
import getpass
import inspect
import sys


class SelfHash:
    """Class for SelfHash"""
    def __init__(self):
        """Init function"""
        self.file_data_hash = None
        self.source_code_hash = None
        self.known_hash = None

    def hash(self, file):
        """Function that hashes the source code"""
        with open(file, 'r', encoding="utf-8") as source_file:
            file_data = source_file.readlines()

        try:
            hash_line_index = [i for i, line in enumerate(file_data) if line.strip().startswith("# Hash:")][0]
        except IndexError:
            print("The '# Hash:' line was not found in the file.")
            print("Please add '# Hash: INSERT_HASH_HERE' at \nthe top of your python file and try again.")
            sys.exit(1)

        self.file_data_hash = ''.join([line for i, line in enumerate(file_data) if i != hash_line_index])

        salt = getpass.getpass(prompt='Please provide a salt for the hash calculation.\nIf you do not want to provide one, just press Enter: ')
        self.file_data_hash += salt

        self.source_code_hash = hashlib.sha256(self.file_data_hash.encode()).hexdigest()

        self.known_hash = file_data[hash_line_index].strip().split(' ')[-1]

        if self.known_hash in ("Hash:", "INSERT_HASH_HERE"):
            print("The hash of the source code is not set yet.\nPlease run the script once and then replace INSERT_HASH_HERE with the hash.")
            print("Hash of the source code:\n", self.source_code_hash)
            sys.exit()
        elif self.known_hash == self.source_code_hash:
            print("\033[92mPASS\033[0m: The program is verified and true.")
        else:
            print("\033[91mFAIL\033[0m: The source code may have been tampered with or the salt/passphrase is incorrect.")
            sys.exit()


def _get_caller_file():
    stack = inspect.stack()
    caller_frame = stack[-1]
    caller_file = caller_frame.filename
    return caller_file

# Automatically hash the caller
SelfHash().hash(_get_caller_file())
