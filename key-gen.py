from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def genkeys(n,p,g):
    sk = random_with_N_digits(n)
    pk = pow(g,sk,p)
    return sk, pk

def sign(sk, msg, p, g):
    d = msg - sk
    sig = pow(g,d,p)
    return sig

def verify(pk, sig, msg, p, g):
    a = pow(g,msg, p)
    b = pow((sig*pk),1,p)
    if(a==b):
        bool = True
    else:
        bool = False
    return bool

# Unit Test
n, g, p = 56, 2, 1332417598677447461893313500475363476151903748659325311025356350620691477624842555612653603

from source import sha_256
from sha_256 import final_hash
m = final_hash

skx, pkx = genkeys(n,p,g)
print("Public Key: ",pkx)

sig= sign(skx,m,p,g)
print("Signed message: ",sig)
if bool == True:
    print(verify(pkx,sig,p,g)," should be True")
if bool == False:
    print(verify(pkx,sig,p,g)," should be False")
