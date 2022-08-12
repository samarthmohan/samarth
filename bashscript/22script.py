def addition(l1,l2):
    len_l1 = len(l1)
    len_l2 = len(l2)
    final_len = 0
    if len_l1 > len_l2:
        final_len = len_l1
    else:
        final_len = len_l2
    addition = []
    flag = 0
    for i in range(final_len):
        if flag>0:
            if (l1[i] + l2[i]) < 10:
                addition.append(l1[i]+l2[i]+1)
            else:
                addition.append(l1[i]+l2[i]-10)
                flag = 1
        else:
            if (l1[i] + l2[i]) < 10:
                addition.append(l1[i]+l2[i])
            else:
                addition.append(l1[i]+l2[i]-10)
                flag = 1
    return addition

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(addition(l1,l2))
