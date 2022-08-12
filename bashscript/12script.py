def solution(sequence):
    sorted_seq = sorted(sequence)
    print sorted_seq
    for i in range(0,len(sorted_seq)-1):
        print str(sorted_seq[i]) + ' ' + str(sorted_seq[i+1])
        if sorted_seq[i] == sorted_seq[i+1]:
            return False
        else:
            return True


sequence = [1, 4, 10, 4, 2]
print(solution(sequence))
