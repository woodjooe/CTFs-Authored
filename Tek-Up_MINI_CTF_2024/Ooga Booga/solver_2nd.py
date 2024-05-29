# Not a very optimized solution for the sake of readability, but should be easy to understand how to solve this challenge


cipher = open('cipher.txt','r').read()
cipher = cipher[2:-2].split("', '")

cipher0 = [bytes.fromhex(c) for c in cipher]

# from the 1st solver we get the correct value of i, this i value helped us determine the position of the 1st 'Palestine ' string.
i = 15

P = cipher0[i]
a = cipher0[i+1]
l = cipher0[i+2]
e = cipher0[i+3]
s = cipher0[i+4]
t = cipher0[i+5]
i_ = cipher0[i+6]
n = cipher0[i+7]
e = cipher0[i+8]
__= cipher0[i+9]


# you should be able to figure this one out in the 1st step | GUESSABLE WORD: the (letters : T, h)
T = cipher0[0]
h = cipher0[1]

# you should be able to figure this one out in the 2nd step | GUESSABLE WORD: history (letters: o, r, y),  of (letters: f)
o = cipher0[8]
r = cipher0[9]
y = cipher0[10]
#o = cipher0[12]
f = cipher0[13]
 
# you should be able to figure this one out in the 3rd step | GUESSABLE WORD: epic (letters: p,c), spanning (letters: g), millenia (letters: m) 
p = cipher0[32]
c = cipher0[34]
g = cipher0[48]
m = cipher0[50]

# Now the flag starts to appear, and you can easily guess the rest or continue to find the last missing letter

S_ = cipher0[1613+0]
#e = cipher0[1613+1]
#c = cipher0[1613+2]
u = cipher0[1613+3]
#r = cipher0[1613+4]
#i = cipher0[1613+5]
#n = cipher0[1613+6]
#e = cipher0[1613+7]
#t = cipher0[1613+8]
#s = cipher0[1613+9]
open_brace = cipher0[1613+10]
close_brace = cipher0[1613+34]



S=''
for j in range(len(cipher0)):
    
    if (cipher0[j]==P):
        S+='P'
    elif (cipher0[j]==a):
        S+='a'
    elif (cipher0[j]==l):
        S+='l'
    elif (cipher0[j]==e):
        S+='e'
    elif (cipher0[j]==s):
        S+='s'
    elif (cipher0[j]==t):
        S+='t'
    elif (cipher0[j]==i_):
        S+='i'
    elif (cipher0[j]==n):
        S+='n'
    elif (cipher0[j]==P):
        S+='e'
    elif (cipher0[j]==__):
        S+=' '
    
# you should be able to figure this one out in the 1st step
    elif (cipher0[j]==T):
        S+='T'
    elif (cipher0[j]==h):
        S+='h'
    
# you should be able to figure this one out in the 2nd step
    elif (cipher0[j]==o):
        S+='o'
    elif (cipher0[j]==r):
        S+='r'
    elif (cipher0[j]==y):
        S+='y'
    elif (cipher0[j]==f):
        S+='f'

# you should be able to figure this one out in the 3rd step
    elif (cipher0[j]==p):
        S+='p'
    elif (cipher0[j]==c):
        S+='c'
    elif (cipher0[j]==g):
        S+='g'
    elif (cipher0[j]==m):
        S+='m'
      
    
# Now the flag starts to appear, and you can easily guess the rest or continue to find the last missing letter
    elif (cipher0[j]==S_):
        S+='S'
    elif (cipher0[j]==u):
        S+='u'
    elif (cipher0[j]==open_brace):
        S+='{'        
    elif (cipher0[j]==close_brace):
        S+='}'
    
    else:
        S+='?'

if(S.count('Palestine ')==8):
    print(S)
