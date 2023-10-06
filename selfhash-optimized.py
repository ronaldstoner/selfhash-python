import hashlib, getpass
# Hash: INSERT_HASH_HERE
file_data = open(__file__, 'r').readlines()
hash_line_index = [i for i, line in enumerate(file_data) if line.strip().startswith("# Hash:")][0]
file_data_hash = ''.join([line for i, line in enumerate(file_data) if i != hash_line_index]) + getpass.getpass(prompt='Salt/Passphrase (press Enter for none): ')
source_code_hash = hashlib.sha256(file_data_hash.encode()).hexdigest()
known_hash = file_data[hash_line_index].strip().split(' ')[-1]
print(("PASS: The program is verified and true." if known_hash == source_code_hash else "FAIL: The source code may have been tampered with.") if known_hash != "INSERT_HASH_HERE" else "The hash of the source code is not set yet.\nPlease run the script once and then replace INSERT_HASH_HERE with the hash.\nHash of the source code:\n" + source_code_hash)
print("The code for this Python script was hashed and the hash of the code is:\n", source_code_hash)