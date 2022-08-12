def solution(sequence):
    k=0
    m=0
    ord_seq = []
    ord_seq = sequence.sort()
    for i in range(0,len(sequence)-1):
       for j in range(i,len(sequence)-1):
           if sequence[i] >= sequence[j]:
               k += 1
    if k > 1:
        return False
    else:
        return True
        
numbers = [1, 2, 1, 3, 4]
solution(numbers)
