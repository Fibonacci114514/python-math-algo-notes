def Bubble_Sort(testlist):
    while True:
        errorcount=0
        for i in range(len(testlist)-1):
            if testlist[i]>testlist[i+1]:
                testlist[i],testlist[i+1]=testlist[i+1],testlist[i]
                errorcount=errorcount+1
        if errorcount==0:
            return testlist
print(Bubble_Sort([14105, 81193, 41299, 6596, 83102, 92049, 55600, 61372, 37117, 60122, 17506, 20742, 71482, 68720, 62817, 1408, 94084, 61621, 98858, 52258]))