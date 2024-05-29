## WriteUp
- Simply find the e th root of the ciphertext
## solver
c = open('cipher.txt','rb').read()
long_to_bytes(nroot(int(c.split(b'CipherText = ')[1].decode(), 16),2539))