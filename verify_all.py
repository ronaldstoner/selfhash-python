#!/usr/bin/python
# Hash: 8a26874511080270877d2b3e5f94191fd9e5fd2dad5a191065906c8e66faa781
# Author: Ron Stoner
# Github: ronaldstoner
# Website: stoner.com

"""Script to verify all Python files in a directory recursively"""

import glob
import selfhash

def hash_and_verify_files(directory):
    """Hash and verify all .py files in the given directory recursively."""
    
    # Find all Python files in the directory and its subdirectories
    py_files = glob.iglob(directory + '**/*.py', recursive=True)
    total_files = sum(1 for _ in py_files)  # Count the total number of .py files
    print(f"\nTotal Python files found: {total_files}")
    
    # Re-run glob to get the file list again after counting
    py_files = glob.iglob(directory + '**/*.py', recursive=True)

    for filename in py_files:
        print(f"\nProcessing {filename}...")
        
        # Instantiate the SelfHash class for each file
        hasher = selfhash.SelfHash(bypass_salt=True)
        
        # Perform the hash verification for each file
        hasher.hash(filename)

        # Check the hash against the known value and display appropriate messages
        if hasher.known_hash == "INSERT_HASH_HERE":
            print(f"\033[93mWARNING\033[0m: The hash is not set for {filename}.")
            print(f"Generated Hash: {hasher.source_code_hash}")
            print("Please replace 'INSERT_HASH_HERE' with the generated hash and run the script again.")
        elif hasher.known_hash == hasher.source_code_hash:
            print(f"Expected Hash: {hasher.known_hash}")
            print(f"Actual Hash: {hasher.source_code_hash}")
        else:
            print(f"\033[91mFAIL\033[0m: The source code of {filename} may have been tampered with or the hash does not match.")
            print(f"Expected Hash: {hasher.known_hash}")
            print(f"Actual Hash: {hasher.source_code_hash}")
            print("Please investigate this file.\n")

    print("\nVerification process complete.")

# Run the verification function starting from the current directory
if __name__ == "__main__":
    hash_and_verify_files("./")
