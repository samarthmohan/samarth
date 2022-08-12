def solution(inputArray):
    multiArray=[]
    for i in range(1,len(inputArray)):
        multiArray.append(inputArray[i-1]*inputArray[i])
    max=0
    for i in multiArray:
        if i>max:
            max=i
    return max

print(solution([3, 6, -2, -5, 7, 3]))
