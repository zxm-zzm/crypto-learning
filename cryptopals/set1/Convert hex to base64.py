string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
binary=bin(int(string,16))[2:].zfill(len(string)*4)
six_group=[binary[i:i+6]for i in range(0,len(binary),6)]
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
last_group_len=len(six_group[-1])

if last_group_len==2:
    six_group[-1]+='0000'
    padding="=="
elif last_group_len==4:
    six_group[-1]+='00'
    padding="="
else:
    padding=""
    
base64_result=[]
for group in six_group:
    index=int(group,2)
    base64_result.append(base64_chars[index])
final_result="".join(base64_result)+padding
print(final_result)