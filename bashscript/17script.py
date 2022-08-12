def solution(inputArray):
    strLen = []
    for word in inputArray:
        strLen.append(len(word))
    print strLen
    maxLen=0
    for i in strLen:
        if i>maxLen:
            maxLen=i
    #print maxLen
    outputArray = []
    for j in range(0,len(strLen)):
        if strLen[j] == maxLen:
            outputArray.append(inputArray[j])
    return outputArray


print(solution(["aba", "aa", "ad", "vcd", "aba"]))
