#Password generator functions which return several different types of passwords and tokens

import secrets
import string
from random_word import RandomWords

# Generate a passphrase in <RandomWord><2-digits><RandomWord><2-digits> format
def generateStudentPassphrase():
    r = RandomWords()
    intSet = string.digits
    word1 = r.get_random_word(minLength=4, maxLength=6, hasDictionaryDef=True)
    word2 = r.get_random_word(minLength=4, maxLength=6, hasDictionaryDef=True)
    digit1 = ''.join(secrets.choice(intSet) for i in range(2))
    digit2 = ''.join(secrets.choice(intSet) for i in range(2))
    passphrase = ''.join([word1, digit1, word2, digit2])
    print(passphrase)

generateStudentPassphrase()

# Generate a 10 character alphanumeric password
def tenCharAlphaNum():
    key = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(key) for i in range(10))
    print('10 character alphanumeric password: ' + password)


# Generate a 10 character alphanumeric password with at least one lowercase character, 
# at least one uppercase character, 
# and at least three digits
def tenCharAlphaNum_Up_Low_three():
    key = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(key) for i in range(10))
        if (any(c.islower() for c in password) and any(c.isupper()
        for c in password) and sum(c.isdigit() for c in password) >= 3):
            print('10 character alphanumeric password with at least one lowercase character,' + '\n' + 'at least one uppercase character, and at least three digits: ' + password)
            break


# Return a random integer from within a given range
def randomInt(range):
    password = secrets.randbelow(range)
    print('random integer: ' + str(password))


# Return a random integer with k random bits
def randomInt_Bits(bits):
    password = secrets.randbits(bits)
    print('random integer with k random bits: ' + str(password))


# Note on Generating Tokens: 
# At least 32 bytes for tokens should be used to be secure against a brute-force attack.


# Generates a random byte string containing nbytes number of bytes. If no value is provided, a reasonable default is used.
def generateTokens_bytes():
    token1 = secrets.token_bytes() 
    token2 = secrets.token_bytes(10) 
    
    print('token with random length: ' + str(token1)) 
    print('token with 10 characters: ' + str(token2))


# Generates a random text string in hexadecimal containing nbytes random bytes. If no value is provided, a reasonable default is used.
def generateTokens_hex():
    token1 = secrets.token_hex() 
    token2 = secrets.token_hex(10) 
    
    print('hexadecimal token with random length: ' + str(token1)) 
    print('hexadecimal token with 10 characters: ' + str(token2))


# Generates a random URL-safe text string containing nbytes random bytes. This is suitable for password recovery applications.
# Example : Generate a hard-to-guess temporary URL containing a security token.
def generateRandomURLToken():
    url = 'https://mydomain.com/reset=' + secrets.token_urlsafe() 
    print('random url with random length: ' + url)
