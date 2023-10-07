#!/usr/bin/python
# Hash: c3cc1ea03ccae7a8a6f33ba3c53b6d2a143311e46a9b16e1b511b543ed27f885

"""Script to verify all python files in a directory recursively"""

import glob
import selfhash

def hash_and_verify_files(directory):
    """Hash and verify all found .py files"""
    # Use glob to find all .py files in the directory and its subdirectories
    for filename in glob.iglob(directory + '**/*.py', recursive=True):
        print(f"Processing {filename}...")

        # Instantiate a new selfhash class for each file
        hasher = selfhash.SelfHash()
        hasher.hash(filename)

        if hasher.known_hash == "INSERT_HASH_HERE":
            print(f"Generated Hash for {filename}: {hasher.source_code_hash}")
            print("Please replace INSERT_HASH_HERE with this hash and run the script again.")
        elif hasher.known_hash == hasher.source_code_hash:
            print(f"PASS: The program {filename} is verified and true.")
        else:
            print(f"FAIL: The source code of {filename} may have been tampered with.")

# Run the function starting from the current directory
hash_and_verify_files("./")
