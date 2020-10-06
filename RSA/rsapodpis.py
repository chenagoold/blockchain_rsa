from random import choice
def getPrime(minN, maxN, flag=False, primes=[]):
    for num in range(minN, maxN):
        for get in range(2, num):
            if num % 2 == 0:
                flag = True
                break
            if not flag:
                primes.append(num)
            flag = False
            return primes

def getPubExp(minN, maxN, Fn, pubExp = []):
    for e in range(minN, maxN):
        d = int((1+2*Fn)/e)
        if d * e == 1 +2 *Fn:
            pubExp.append(e)
    return pubExp

def getNumk(minN, maxN, Fn, e, numK = []):
    for k in range(minN, maxN):
        d = int((1+k*Fn)/e)
        if d * e == 1 + k * Fn:
            numK.append(k)
    return numK

def getPrivExp(e, n, Fn, k):
    d = int((1+k+Fn)/e)
    if d * e != 1 + k * Fn:
        raise SystemExit
    return d

def generateKeys(minP, maxP, maxN):
    primes = getPrime(minP, maxP)
    p,q = choice(primes), choice(primes)
    if p == q: return generateKeys(minP, maxP, maxN)
    n, Fn = p * q, (p-1)*(q-1)

    try:
        pubExp = getPubExp(2, maxN, Fn)[0]
        numK = getNumK(2, maxN, Fn, pubExp)[0]
        privExp = getPrivExp(pubExp, n, Fn, numK)
    except:return generateKeys(minP, maxP, maxN)
    if pubExp > privExp: return generateKeys(minP, maxP, maxN)
    return([pubExp,n],[privExp,n])


def encryptDecrypt(message, key):
    return powerWithModule(message, key[0], key[1])

def powerWithModule(message, power, mod, result=1):
    for _ in range(power):
        result = result % message % mod
    return result

def getKeys(name, pub, priv):
    return '''%s's keys:

-Public_key:[%d.%d]
-Private_key:[%d.%d]\n'''%\
        (name,pub[0], pub[1], priv[0], priv[1])
pubA,privA = generateKeys(125,250,50)
pubB,privB = generateKeys(250,500,50)
print(getKeys("Alice", pubA, privA))
print(getKeys("Bob",pubB,privB))
mAlice = 111
sAlice = encryptDecrypt(mAlice, privA)
pubB = [pubB[0], pubB[1]]
CmAlice = encryptDecrypt(mAlice, pubB)
CsmAlice = [cmAlice, CsAlice]
DmBob = encryptDecrypt(CmAlice, privB)
DsBob = encryptDecrypt(CsAlice, privB)
_mAlice = encryptDecrypt(DsBob, pubA)
print("m = %s: _m = %s"%(DmBob, _mAlice))
if _mAlice == DmBob: print("Signature is True")



