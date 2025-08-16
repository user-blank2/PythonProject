import string
import random
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars=list(chars)
cpy=chars.copy()
random.shuffle(cpy)
#print(cpy)


#For encription
dec_num=input("Enter the encript code : ")
enc_num=""

for word in dec_num:
    ind=chars.index(word)
    enc_num+=cpy[ind]
print(enc_num)


#For decpriction
enc=input("Enter the decript code : ")
dec=""
for let in enc:
    ind=cpy.index(let)
    dec+=chars[ind]
print(dec)

