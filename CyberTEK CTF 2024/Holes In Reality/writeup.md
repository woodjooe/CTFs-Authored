## WriteUp

```python
# Equals a number x1 thats a multiple of P
x1 = A[1]^2 - B[1]^2 - A[0]^3 - 47711*A[0] + B[0]^3 + 726*B[0]
# Equals a number x2 thats a multiple of P
x2 = A[1]^2 - G[1]^2 - A[0]^3 - 47711*A[0] + G[0]^3 + 726*G[0]

P = gcd(x1, x2)
```

Now we have the prime number P and therefore we have the elliptic curve.

Calculating the order of G in the elliptic curve turns out to be a small number (around 5 digits). Therefore, regardless of what A and B are, we can easily bruteforce the Point C in the elliptic curve which allows us to get all the possible AES cipher keys in a short amount of time and decrypt the ciphertext using each one of them.