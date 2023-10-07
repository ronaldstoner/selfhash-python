#!/usr/bin/python
# Hash: 2f2f37bb2c52daf7cec82c31467891e62085eeabd786a466a20295cc788e7190

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
