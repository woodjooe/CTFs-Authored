from Crypto.Util.number import *
from random import randint
e= 65537


def generate_prime(p):
    while(True):
        p += 1 
        if(isPrime(p)):
            break
    return p


P = randint(1,2**513 - 1)
Q = generate_prime(P)
P = generate_prime(Q) 

N = P * Q

flag = open('message.txt', 'rb').read()

ciphertext = hex(pow(bytes_to_long(flag), e, N))[2:]

public_key = f"Public Key = [{N}, {e}]"
ciphertext = f"CipherText = {ciphertext}"

file = open('cipher.txt','w')
file.writelines(public_key + '\n')
file.writelines(ciphertext)
