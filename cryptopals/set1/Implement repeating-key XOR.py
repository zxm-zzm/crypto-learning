plaintext=b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key=b"ICE"
ciphertext=bytes([p^key[i%len(key)]for i,p in enumerate(plaintext)])
print(ciphertext.hex())