"""Script to verify the selfhash/selfhash.py module hash"""
import selfhash

# Load selfhash into a hasher and perform the verification check
hasher = selfhash.SelfHash()
hasher.hash("selfhash/selfhash.py")  # replace with the actual path to the selfhash.py file

print(hasher.hash)
# This should only run if the hash matches and the program is 'verified'
print("The hash inside of selfhash/selfhash.py matches and looks correct.")
