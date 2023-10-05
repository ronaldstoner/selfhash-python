# selfhash-python
A self-hashing python script that provides a very simple hashed code check

# Initial run
The script must be ran for the first time in order to generate an initial hash.

<img src="https://github.com/ronaldstoner/selfhash-python/blob/main/img/1.png?raw=true" /> 

# Adding the known good hash
The known good hash should then be added to `KNOWN_HASH` string in the script

<img src="https://github.com/ronaldstoner/selfhash-python/blob/main/img/2.png?raw=true" /> 

# Verifying the script on execution[

<img src="https://github.com/ronaldstoner/selfhash-python/blob/main/img/3.png?raw=true" /> 

# Tampering with the script
Making a change in the script will result in a new hash

<img src="https://github.com/ronaldstoner/selfhash-python/blob/main/img/4.png?raw=true" />

# Failing the verification check
If `KNOWN_HASH` != `hash` then fail

<img src="https://github.com/ronaldstoner/selfhash-python/blob/main/img/5.png?raw=true" />

# Future
- modularize it
- better immutable way to store hash
- set known good hash for this script itself 
