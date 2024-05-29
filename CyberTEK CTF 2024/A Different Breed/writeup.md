
## WriteUp
1ST STEP: LEAK THE AES IV

-------
encrypt message =  '61616161626262626363636364646464'   ( = b'aaaabbbbccccdddd' ) 
result: ciphertext = b'\x03\xae\x18=\x89Y+9\x07\xe8\xd0\xaa\xea\xcb\xf5\xd3'

------- next:
encrypt: message ='61616161626262626363636364646464' + hex(int(ciphertext.hex(),16)^int(message.hex(),16))[2:]
result: ciphertext = b'\x03\xae\x18=\x89Y+9\x07\xe8\xd0\xaa\xea\xcb\xf5\xd3PYN\xaeF\xb9\x08\xd4\x8b\nON\x8e\xadh\xb6'

------- next:
decrypt: ciphertext[16 :] = b'PYN\xaeF\xb9\x08\xd4\x8b\nON\x8e\xadh\xb6'
result: plaintext = b'\x00\x06\x13\x00\x0c\x06\r\x0f\x0f\x1a3\x0f\x05\x07\x01\x00'

-------
=> IV =long_to_bytes(int(plaintext.hex(),16)^int('61616161626262626363636364646464',16))
=> IV = long_to_bytes(int(b'\x00\x06\x13\x00\x0c\x06\r\x0f\x0f\x1a3\x0f\x05\x07\x01\x00'.hex(),16)^int('61616161626262626363636364646464',16))


2ND STEP:  FACTOR N

Knowing the IV, you know the 2nd half of the flag and therefore the 128*3 most significant bits of one of the prime numbers. 
Knowing these few bits, you can optimize factorisation of N and then get the value of the primes P and Q.
knowing the values of P and Q you can convert them to bytes. 
And deduce your flag ! (classic RSA decryption)
