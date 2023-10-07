#!/usr/bin/python
# Hash: INSERT_HASH_HERE

"""Test file to check hash generation and verification"""

import selfhash

# Load selfhash into a hasher and perform the verification check
hasher = selfhash.SelfHash()
hasher.hash(__file__)

# This should only run if the hash matches and the program is 'verified'
print("This should only print if the hash matches and the program is 'verified'")
