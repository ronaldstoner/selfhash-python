import hashlib
import getpass

class SelfHash:
    def __init__(self):
        self.file_data_hash = None
        self.source_code_hash = None
        self.known_hash = None

    def hash(self, file):
        with open(file, 'r') as source_file:
            file_data = source_file.readlines()
            
        hash_line_index = [i for i, line in enumerate(file_data) if line.strip().startswith("# Hash:")][0]
        self.file_data_hash = ''.join([line for i, line in enumerate(file_data) if i != hash_line_index])

        salt = getpass.getpass(prompt='Please provide a salt/passphrase for the hash calculation. If you do not want to provide one, just press Enter: ')
        self.file_data_hash += salt

        self.source_code_hash = hashlib.sha256(self.file_data_hash.encode()).hexdigest()

        self.known_hash = file_data[hash_line_index].strip().split(' ')[-1]

        if self.known_hash == "INSERT_HASH_HERE":
            print("The hash of the source code is not set yet. Execution cancelled.\nPlease run the script once and then replace INSERT_HASH_HERE with the hash.")
            print("Hash of the source code:\n", self.source_code_hash)
            exit(1)
        elif self.known_hash == self.source_code_hash:
            print("PASS: The program is verified and true.")
        else:
            print("FAIL: The source code may have been tampered with. Execution cancelled.")
            exit(1)
