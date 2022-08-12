def palindrome(num):
    num_str = str(num)
    flag = 0
    rev_num_str = num_str[::-1]
    for i in range(len(num_str)):
        if num_str[i] != rev_num_str[i]:
            flag += 1
    if flag == 0:
        print "palindrome"
    else:
        print "not a palindrome"

x = -121
palindrome(x)
