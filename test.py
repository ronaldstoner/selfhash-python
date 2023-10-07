#!/usr/bin/python
# Hash: c7f962b5cde0cc68174ca405e52742f25d5a08ec78e900b642824b02a6b298b8

"""Test file to check hash generation and verification"""

import selfhash

# Load selfhash into a hasher and perform the verification check
hasher = selfhash.SelfHash(bypass_salt=False)
hasher.hash(__file__)

# This should only run if the hash matches and the program is 'verified'
print("This should only print if the hash matches and the program is 'verified'")
