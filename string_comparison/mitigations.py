import time
import hashlib

N = 1000000
words = [b"airline", b"airline", b"offense", b"defense", b"feature", b"partial"]
l = len(words[0])
lhash = len(hashlib.sha256(words[0]).digest())
samechars = [sum(i) for i in [[k==l for k,l in zip(words[2*m], words[2*m+1])] for m in range(len(words)//2)]]
samecharshash = [sum(i) for i in [[k==l for k,l in zip(hashlib.sha256(words[2*m]).digest(), hashlib.sha256(words[2*m+1]).digest())] for m in range(len(words)//2)]]

def compareStringsMit1(str1, str2):
    padding = b' '*32
    result = True

    str1 = (str1 + padding)[:len(padding)]
    str2 = (str2 + padding)[:len(padding)]

    for i in range(len(padding)):
        if str1[i] != str2[i]:
            result = False

    return result

def compareStringsMit2(str1, str2):
    str1 = hashlib.sha256(str1).digest()
    str2 = hashlib.sha256(str2).digest()

    result = True

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            result = False

    return result

def compareStringsMit3(str1, str2, length):
    result = 1

    for i in range(length):
        result &= (str1[i] == str2[i])

    return result


for i in range(3):
    print("\nMitigation", i)
    for j in range(3):
        r = []
        for _ in range(N):
            s1 = words[j*2]
            s2 = words[j*2+1]
            if i==0:
                a = time.time_ns()
                result = compareStringsMit1(s1, s2)
                b = time.time_ns()
            elif i==1:
                a = time.time_ns()
                result = compareStringsMit2(s1, s2)
                b = time.time_ns()
            else:
                a = time.time_ns()
                result = compareStringsMit3(s1, s2, l)
                b = time.time_ns()
            c = b - a
            r+=[c]
        print(words[j*2].decode(), words[j*2+1].decode(), "|", min(r), "ns |", "difference:", l - samechars[j], "| difference in hash: ", lhash - samecharshash[j])
