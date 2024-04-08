import hashlib
import ssl
import binascii
import os

global generator
global prime
global key_length

prime = 0xFFFFFFFFFFFFFFFFC90FDAA2216
generator = 2
key_length = 600
# implementation of hellman-algorithm
def generate_private_key(length):
    _rand = 0
    _bytes = length // 8 + 8
    # Generate a random private key such that it's less than the prime number
    while (_rand.bit_length() < length):
        # TODO: Can use Crypto library hash functions
        hex_key = binascii.b2a_hex(os.urandom(_bytes))
        # Convert to denary format
        _rand = int(hex_key, 16)
    # Update object
    private_key = _rand
    return private_key


#Public key = primitive root ^ private key % prime
def generate_public_key(private_key):
	public_key = pow(generator, private_key, prime)
	return public_key

#Secret key = public key ^ private key % q
def generate_secret(private_key, public_key):
    # Formula
    secret = pow(public_key, private_key, prime)
    # Generate hash key using SHA256
    key = hashlib.sha256()
    key.update(int.to_bytes(secret, (secret.bit_length() + 7) // 8, byteorder='big'))
    secretKey = key.hexdigest()
    return secretKey

def main():
    # Generate private key
    private_key = generate_private_key(key_length)
    print("Private Key:", private_key)

    # Generate public key
    public_key = generate_public_key(private_key)
    print("Public Key:", public_key)

    # Calculate secret key
    secret_key = generate_secret(private_key, public_key)
    print("Secret Key:", secret_key)

if __name__ == "__main__":
    main()