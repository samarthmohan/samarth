
def romanToNum(roman):
    key={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    n = len(roman)
    finalInt = key[roman[n-1]]
    #print finalInt
    for i in range(n-2,-1,-1):
        #print i
        #print (roman[i])
        if key[roman[i]] < key[roman[i+1]]:
            #print ('if ' + str(roman[i]) + ' < ' + str(roman[i+1]))
            finalInt -= key[roman[i]]
        if key[roman[i]] >= key[roman[i+1]]:
            finalInt += key[roman[i]]
    print finalInt
s = "MCMXCIV"
romanToNum(s)
