def solution(statues):
    output = sorted(statues)
    total = 0
    for i in range(0,len(output)-1):
        total += output[i+1]-output[i]-1
    return total

print(solution([6, 2, 3, 8]))
