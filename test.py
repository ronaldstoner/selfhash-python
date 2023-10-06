# Hash: 5e5154d5554457d1700ee1cc32d7cf848376dc0fdf0a12eb5d8dc282b822b545
import selfhash

# Load selfhash into a hasher and perform the verification check
hasher = selfhash.SelfHash()
hasher.hash(__file__)

# This should only run if the hash matches and the program is 'verified'
print("This should only print if the hash matches and the program is 'verified'")

