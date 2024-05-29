from Crypto.Util.number import *
from libnum import nroot


ciphertext = '37209c93631df888d11a9d02b698ef8bd15b78b20996598e9bc7bc2134a20041d67b3ec821a6871250369112e44e93486d2f5bc04cbacebae6ecdbfb5f7e1ae89df818b5fb9c139a894c2419ed3e90155a9d9a3cb56c93604751a930b79351c708b9f8bc177206be2c16e83bbfaa53e4ce0e9fd8a976ccf2e73428f2b0a2b42f57f614538e04c9d66dd43cf39fb3386d285ef9fefd8e4ddb9face76035a20b1a78e3231c6c0a1fe23a4e7313e0b0b8803a5c552998f426ea9a925b3b70c486fd532519e15b2ceb894a7022fc00701fe921263414ce2c14d80a9c69831192a17052b5598f4631a6799dac94c39b8e1e7f7bab35d1ff024b70d2b05ce9ee776965374'         # insert hex ciphertext here
N =       64882371287055168138489252305916578587281262421004533723031307779871932861303069541247974633365370576102209749574908194809018063247048295720709201280564378872532533547302970151867228753499591203739425315139143726957519510743220070949741293873470575089706489704238738070287395770067048112363327463010294266567907549057796088207569677042992167763117193871290209999847933662273436676167737488501678761136967840904890512812290107146866803380351863883621575966476148477165491791530579803407897212474386302058822209641920448081417089620165966919635214374274622741523278967802934754321923262320963950273495744885827227080150049              # insert public key N here (the modulus)
e = 65537
def generate_prime(p):
    while(True):
        p += 1 
        if(isPrime(p)):
            break
    return p

p0 = nroot(N//(7*5*5*3*3*3), 4)
p1 = p0
for i in range(100000):
  if((N%p1 == 0) and (isPrime(p1))):
    print('Found')
    break
  p1 -= 1
p2 = generate_prime(p1 * 3) 
p3 = generate_prime(p2 * 5)
p4 = generate_prime(p3 * 7)
phi = (p1-1)*(p2-1)*(p3-1)*(p4-1)
flag = long_to_bytes(pow(int(ciphertext,16), inverse(e, phi), N))
print(flag)