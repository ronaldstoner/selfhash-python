#!/usr/bin/python
# Hash: 7133c3ec57f1dbdd2b35a409abebd34ea0736fde377056706b32bf955ae7d313
# Author: Ron Stoner
# Github: ronaldstoner
# Website: stoner.com

# No password is set for this hash as it is used to verify the selfhash module code itself
# This can be checked against the GitHub repository

"""SelfHash - Self-hashing and verification Python script"""

import hashlib
import getpass
import sys


class SelfHash:

    """Class to handle the self-hashing and verification of Python source code."""
    def __init__(self, bypass_salt=False):
        """
        Initializes the SelfHash object.
        
        :param bypass_salt: Flag to bypass the salt input (default is False).
        """
        self.file_data_hash = None      # Holds the hash of the file data without the hash line
        self.source_code_hash = None    # Holds the calculated hash of the source code
        self.known_hash = None          # Holds the known hash from the source code
        self.bypass_salt = bypass_salt  # Flag to bypass the salt input

    def hash(self, file):
        """
        Reads the file, calculates its hash, and verifies the integrity of the code by comparing
        it with the known hash embedded in the source.
        
        :param file: The Python file to be hashed and verified.
        """
        fail = False

        # Open the file and read its contents into a list of lines
        with open(file, 'r', encoding="utf-8") as source_file:
            file_data = source_file.readlines()

        # Ensure the file has at least 2 lines (the second line will contain the hash)
        if len(file_data) < 2:
            print("Error: The file is too short. It should have at least 2 lines.")
            fail = True
            sys.exit(1)  # Exit immediately if the file is too short

        # Extract the hash from the line and fail if not found
        try:
            hash_line_index = [i for i, line in enumerate(file_data) if line.strip().startswith("# Hash:")][0]
        except IndexError:
            print("The '# Hash:' line was not found in the file.")
            print("Please add '# Hash: INSERT_HASH_HERE' at \nthe top of your python file and try again.")
            fail = True
            sys.exit(1) # Exit immediately if the '# Hash: ' is not found

        # Remove the hash line from the source file data to compute the rest of the code's hash
        self.file_data_hash = ''.join([line for i, line in enumerate(file_data) if i != hash_line_index])

        # Prompt for a salt if not bypassing it
        if not self.bypass_salt:
            salt = getpass.getpass(prompt='This python script is protected by SelfHash.\nPlease provide a salt for the hash calculation.\nIf you do not want to provide one, just press Enter: ')
            if salt:  # If a salt is provided, add it to the file data hash
                self.file_data_hash += salt

        # Calculate the SHA-256 hash of the source code (with salt if provided)
        self.source_code_hash = hashlib.sha256(self.file_data_hash.encode()).hexdigest()

        # Compare the known hash to the calculated hash
        self.known_hash = file_data[hash_line_index].strip().split(' ')[-1]
        self.known_hash = self.known_hash.strip()  # Clean up extra spaces

        if len(self.known_hash) != 64:  # Ensure it is a valid SHA256 hash
            print("Invalid hash format found in the file.")
            fail = True

        if self.known_hash in ("Hash:", "INSERT_HASH_HERE"):
            print("The hash of the source code is not set yet.\nPlease run the script once and then replace INSERT_HASH_HERE with the hash.")
            print("Hash of the source code:\n", self.source_code_hash)
            fail = True
        elif self.known_hash == self.source_code_hash:
            print("\033[92mPASS\033[0m: The program is verified and true.")
        else:
            print("\033[91mFAIL\033[0m: The source code may have been tampered with or the salt/passphrase is incorrect.")
            fail = True

        # Exit with error if there was any failure
        if fail:
            sys.exit(1)
