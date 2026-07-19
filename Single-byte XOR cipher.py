string="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ciphertext = bytes.fromhex(string)
for key in range(256):
    result=bytes([b^key for b in ciphertext])
    if ord('a')<=result[0]<=ord('z') or ord('A')<=result[0]<=ord('Z'):
        print(result,key)
    else:
        continue
    

