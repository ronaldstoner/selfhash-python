# SelfHash

SelfHash is a Python package that allows you to hash your Python scripts and verify them. It's designed to provide an additional layer of security by ensuring that your script's code has not been tampered with. If the hash does not match the known good hash then the script will immediately exit and prevent further execution.

## Installation

You can install SelfHash from source with:

```bash
git clone https://github.com/ronaldstoner/selfhash-python.git
cd selfhash-python
pip install .
```

## Integrating SelfHash Into Your Scripts

To use SelfHash in your scripts, you need to follow two steps:

1. **Add the Hash Line:** At the top of your script file, include the following special line of code: `# Hash: INSERT_HASH_HERE`. This line serves as a placeholder for the hash of your script's code. 

2. **Use the SelfHash Module:** Import the SelfHash module in your script, create a new instance of the SelfHash class, and then call the `hash` method on this instance, passing `__file__` as an argument. This will calculate the hash of your script and verify it against the stored hash.

Here's an example:

```python
# Hash: INSERT_HASH_HERE
import selfhash

hasher = selfhash.SelfHash()
hasher.hash(__file__)
```

When you run a script that uses SelfHash for the first time, it will generate a hash of the script. You then need to insert this hash into the `# Hash: ` comment (leave it commented) of the script's code. This hash is then used for verification in subsequent runs.

If the hash of the script matches the known good hash, the script will print `PASS: The program is verified and true.` and continue execution. If the hash does not match, the script will print `FAIL: The source code may have been tampered with.` and immediately exit.

## Salt/Passphrase

When you run the `hash` method, it will prompt you to enter a salt/passphrase for the hash calculation. This is an optional step that you can use to add an extra layer of security to your hash. 

If you choose to provide a salt/passphrase, it will be used in the calculation of the hash of your script. This means that even if someone else has the exact same script code, they won't be able to generate the same hash unless they also know your salt/passphrase. 

If you choose not to provide a salt/passphrase, you can simply press Enter when prompted and the hash will be calculated based only on your script's code.

Remember - if you use a salt/passphrase you should use the same salt/passphrase every time you run the script, otherwise the hash will be different and the script will fail the verification. This salt/passphrase should be stored securely for future retrieval.

## Verifying The SelfHash Module

To ensure the integrity of the SelfHash module itself, we provide a script named `verify_self.py`. This script uses SelfHash to verify the hash of the `selfhash/selfhash.py` file.

If the hash of `selfhash/selfhash.py` matches the known hash at the top of the file, `verify_self.py` will print a message saying, `The hash inside of selfhash/selfhash.py matches and looks correct.`

To run `verify_self.py`, use the following command without any salt (no passphrase is set):

```bash
python verify_self.py
```

## Screenshots
### Hashing A Script For The First Time
<img src="https://github.com/ronaldstoner/selfhash-python/blob/main/img/1.png?raw=true" />

### Verifying The Hash And Executing
<img src="https://github.com/ronaldstoner/selfhash-python/blob/main/img/2.png?raw=true" />

### Preventing Execution Of A Modified Script Or Incorrect Salt
<img src="https://github.com/ronaldstoner/selfhash-python/blob/main/img/3.png?raw=true" />
