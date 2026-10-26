import random
def staggeredfunction(s):
    while True:
        staggerederrorcount=0
        random.shuffle(s)
        for i in range(len(s)):
            if i==s[i]:
                staggerederrorcount+=1
        if staggerederrorcount==0:
            return s
l=4
s=[x for x in range(l)]
s0=[x for x in range(l)]
while True:
    reflector={}
    reflectorerrorcount=0
    reflector=dict(zip(s0, staggeredfunction(s)))
    for i in range(l):
        if reflector[reflector[i]]!=i:
            reflectorerrorcount+=1
    if reflectorerrorcount==0:
        break
print(reflector)