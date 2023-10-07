#!/usr/bin/python
# Hash: ff09080b23d744ebcc446a3fdce8dc0da5ae1b127517a4d29c3be46219a012c4

"""Script to verify all python files in a directory recursively"""

import glob
import selfhash

def hash_and_verify_files(directory):
    """Hash and verify all found .py files"""
    # Use glob to find all .py files in the directory and its subdirectories
    for filename in glob.iglob(directory + '**/*.py', recursive=True):
        print(f"Processing {filename}...")

        # Instantiate a new selfhash class for each file
        hasher = selfhash.SelfHash(bypass_salt=True)
        hasher.hash(filename)

        if hasher.known_hash == "INSERT_HASH_HERE":
            print(f"Generated Hash for {filename}: {hasher.source_code_hash}")
            print("Please replace INSERT_HASH_HERE with this hash and run the script again.")
        elif hasher.known_hash == hasher.source_code_hash:
            print(f"\033[92mPASS\033[0m: The program {filename} is verified and true.")
        else:
            print(f"\033[91mFAIL\033[0m: The source code of {filename} may have been tampered with.")

# Run the function starting from the current directory
hash_and_verify_files("./")
