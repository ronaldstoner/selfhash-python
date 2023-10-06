# Hash: f33b4b92aead8881ff6489aa61d5c850cb34589d9e86a99bae69bfa10eafd7ee
# No password is set for this hash as it is used to verify the selfhash module code itself and can be checked against the github repo
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
        
        try:
            hash_line_index = [i for i, line in enumerate(file_data) if line.strip().startswith("# Hash:")][0]
        except IndexError:
            print("The '# Hash:' line was not found in the file.")
            print("Please add '# Hash: INSERT_HASH_HERE' at the top of your python file and try again.")
            exit(1)
        
        self.file_data_hash = ''.join([line for i, line in enumerate(file_data) if i != hash_line_index])

        salt = getpass.getpass(prompt='Please provide a salt for the hash calculation. If you do not want to provide one, just press Enter: ')
        self.file_data_hash += salt

        self.source_code_hash = hashlib.sha256(self.file_data_hash.encode()).hexdigest()

        self.known_hash = file_data[hash_line_index].strip().split(' ')[-1]

        if self.known_hash == "INSERT_HASH_HERE":
            print("The hash of the source code is not set yet.\nPlease run the script once and then replace INSERT_HASH_HERE with the hash.")
            print("Hash of the source code:\n", self.source_code_hash)
            exit(1)
        elif self.known_hash == self.source_code_hash:
            print("PASS: The program is verified and true.")
        else:
            print("FAIL: The source code may have been tampered with.")
            exit(1)