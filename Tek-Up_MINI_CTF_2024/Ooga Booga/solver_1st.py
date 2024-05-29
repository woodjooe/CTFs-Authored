cipher = open('cipher.txt','r').read()
cipher = cipher[2:-2].split("', '")
print(cipher[0])
cipher0 = [bytes.fromhex(i) for i in cipher]
k = 0
for i in range(len(cipher0)-9):
    P = cipher0[i]
    a = cipher0[i+1]
    l = cipher0[i+2]
    e = cipher0[i+3]
    s = cipher0[i+4]
    t = cipher0[i+5]
    I = cipher0[i+6]
    n = cipher0[i+7]
    e = cipher0[i+8]
    __= cipher0[i+9]
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
        elif (cipher0[j]==I):
            S+='i'
        elif (cipher0[j]==n):
            S+='n'
        elif (cipher0[j]==P):
            S+='e'
        elif (cipher0[j]==__):
            S+=' '
        else:
            S+='?'
            
    if(S.count('Palestine ')==8):
        print(S)
        print(i)
        k +=1
print('number of possible partial plaintexts = ',k) #should be >= to the amount of times 'Palestine ' has been mentioned
#print(open('message.txt','r').read())
