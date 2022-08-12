def solution(n):
    subtotal=0
    for i in range(0,n):
        subtotal += i
    print subtotal
    area=1+(4*(subtotal))
    return area
print(solution(3))
