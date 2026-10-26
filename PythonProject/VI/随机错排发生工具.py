import random
s=[0,1,2,3,4]
while True:
    errorcount=0
    random.shuffle(s)#打乱
    for i in range(len(s)):
        if i==s[i]:
            errorcount+=1
    if errorcount==0:
        break#检测是否错排
print(s)