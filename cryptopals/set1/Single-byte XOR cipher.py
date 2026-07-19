string="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ciphertext = bytes.fromhex(string)
def count(result):
    try:
        s=result.decode('ascii')
    except UnicodeDecodeError:
        return 0
    letter=sum(1 for c in s if c.isalpha())
    space=sum(1 for c in s if c.isspace())
    return letter+space

best=0
best_key=None
best_message=""
for key in range(256):
    result=bytes([b^key for b in ciphertext])
    new=count(result)
    if new>best:
        best=new
        best_key=key
        best_message=result
print(best_key,best_message)