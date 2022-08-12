def romtonum(rom):
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    #print dict
    #print type(dict)
    num=0
    rom_brk=[]
    rom_brk[:]=rom
    #print rom_brk
    #print (type(rom_brk))
    frag=[]
    i=0
    if (len(rom_brk)%2==0):
        while i<len(rom_brk):
            #num+=dict[i]
            frag.append(rom_brk[len(rom_brk)-i-2:len(rom_brk)-i])
            i+=2
        print frag
    else:
        while i<=len(rom_brk):
            #num+=dict[i]
            frag.append(rom_brk[len(rom_brk)-i-2:len(rom_brk)-i])
            i+=2
        frag.append(rom_brk[0])
        print frag

    #print num
    return rom_brk

romtonum('MCMXCIV')
