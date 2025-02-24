#!/usr/bin/python3
# Hash: b3bdd013f179bb06e9be80e8282c3d3dcaf34463f33257b88a96769daf51689c 
# Author: Ron Stoner
# Github: ronaldstoner
# Website: stoner.com

"""Script to verify the selfhash/selfhash.py module hash"""

import selfhash

def verify_selfhash():
    """Verifies the hash of the selfhash.py module."""
    
    # Instantiate the SelfHash class with bypass_salt=True to skip salt prompt
    hasher = selfhash.SelfHash(bypass_salt=True)
    
    # Perform the hash verification check on the selfhash.py module
    print("\nVerifying the hash of the 'selfhash/selfhash.py' module...")
    hasher.hash("selfhash/selfhash.py")  # Replace with the actual path to selfhash.py if needed
    
    # Output the calculated hash and comparison results
    print("Expected Hash: ", hasher.known_hash)
    print("Actual Hash: ", hasher.source_code_hash)
    if hasher.known_hash != hasher.source_code_hash:
        print("\033[91mFAIL\033[0m: The selfhash.py module has been tampered with or the hash does not match.")
        print("Expected Hash: ", hasher.known_hash)
        print("Actual Hash: ", hasher.source_code_hash)
        exit(1)
    elif hasher.known_hash in ("INSERT_HASH_HERE", "Hash:"):
        print("\033[93mWARNING\033[0m: The hash is not set yet. Please replace 'INSERT_HASH_HERE' with the calculated hash.")
        print("Generated Hash: ", hasher.source_code_hash)
        exit(1)
    print("\nVerification complete.")

# Run the verification function
if __name__ == "__main__":
    verify_selfhash()

