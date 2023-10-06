import hashlib
import getpass

# Placeholder for the hash
# This line is used to compare the sourcecode hash but does not include the commented line to prevent a hash != newhashed_code update problem
# Hash: INSERT_HASH_HERE

# Add a value here to make the script fail
ADD_TO_THIS_FOR_FAIL = ""

# Read the source code of the script
with open(__file__, 'r') as source_file:
    file_data = source_file.readlines()

# We'll calculate the hash without the hash line
hash_line_index = [i for i, line in enumerate(file_data) if line.strip().startswith("# Hash:")][0]
file_data_hash = ''.join([line for i, line in enumerate(file_data) if i != hash_line_index])

# Ask the user for a salt
salt = getpass.getpass(prompt='Please provide a salt for the hash calculation. If you do not want to provide one, just press Enter: ')
file_data_hash += salt

# Calculate the hash of the source code
source_code_hash = hashlib.sha256(file_data_hash.encode()).hexdigest()

# Extract the known hash from the hash line
known_hash = file_data[hash_line_index].strip().split(' ')[-1]

# Compare the calculated hash with the known hash
if known_hash == "INSERT_HASH_HERE":
    print("The hash of the source code is not set yet.\nPlease run the script once and then replace INSERT_HASH_HERE with the hash.")
    print("Hash of the source code:\n", source_code_hash)
elif known_hash == source_code_hash:
    print("PASS: The program is verified and true.")
else:
    print("FAIL: The source code may have been tampered with.")

# Print the explanation
print("The code for this Python script was hashed and the hash of the code is:\n", source_code_hash)