#!/usr/bin/python
# Hash: 48717260d6a313c4cc1b3d361a852a34bd24e8ba2786c2a08ecfdaf7f1e556c2

"""Script to verify the selfhash/selfhash.py module hash"""

import selfhash

# Load selfhash into a hasher and perform the verification check
hasher = selfhash.SelfHash(bypass_salt=True)
hasher.hash("selfhash/selfhash.py")  # replace with the actual path to the selfhash.py file

print(hasher.hash)
# This should only run if the hash matches and the program is 'verified'
print("The hash inside of selfhash/selfhash.py matches and looks correct.")
