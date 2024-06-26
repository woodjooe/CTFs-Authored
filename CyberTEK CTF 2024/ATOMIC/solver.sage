from sage.all import matrix, Zmod

# The solution for this challenge is better understood after reading the following paper: https://www.gcsu.edu/sites/files/page-assets/node-808/attachments/pangia.pdf   Enjoy !
N = 25485718648427204748267954075457791484964314848695037606543112745936333092261 # INSERT MODULUS HERE

ciphertexts = [[18586262729540537315634514852790251715780525877362973521285468600526989479910, 10248870675941596878805375350166670685216944135137337256822033398811009203879],[10001103766527596996405589931460079437127601948665912741630345251377076091785, 512003619080500009069021559475149864219133468562566795640279557195143866406]]# [Ciphertext List here]


e = 65537

ciphertexts = matrix(Zmod(N), ciphertexts)

f = factor(N)

primes = []
for i in f:
  primes.append(i[0])

PHI = 1
for p in primes:
  PHI *= (p**2 - p)*(p**2 - 1)


print(primes)

d = int(pow(e, -1, PHI))

plaintexts = ciphertexts ** d

flag = b''
for row in plaintexts:
    for num in row:
        flag += bytes.fromhex((len(hex(num))%2)*'0' + hex(num)[2:])

print(flag)
