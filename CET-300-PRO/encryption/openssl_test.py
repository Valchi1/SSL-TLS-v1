from OpenSSL import crypto

# Encrypt and Decrypt Functions
def encrypt(data, public_key):
    return crypto.sign(public_key, data, 'sha256')

def verify(data, signature, public_key):
    try:
        crypto.verify(public_key, signature, data, 'sha256')
        print("Verification Successful: Data is intact and valid.")
    except crypto.Error as e:
        print("Verification Failed: Data is corrupted or signature is invalid.")

# Main Code
if __name__ == "__main__":
    # Generate a key pair
    key_pair = crypto.PKey()
    key_pair.generate_key(crypto.TYPE_RSA, 2048)

    # Original data to encrypt
    original_data = b"This is the data I want to encrypt"

    # Encrypt the data
    signature = encrypt(original_data, key_pair)

    # Verify the signature
    verify(original_data, signature, key_pair)
