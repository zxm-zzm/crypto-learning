string_1="1c0111001f010100061a024b53535009181c"
string_2="686974207468652062756c6c277320657965"
binary_1=int(string_1,16)
binary_2=int(string_2,16)
result=hex(binary_1^binary_2)[2:].zfill(len(string_1))
print(result)
