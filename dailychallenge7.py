def decode(s):
    l = len(s)
    count = [0 for i in range(l+1)]
    print(count)
    count[0] = 1
    count[1] = 1

    for i in range(2,l+1):
        print(s[i-1])
        if s[i-1]>'0':
            count[i] = count[i-1]

        if s[i-2]<'2' or (s[i-2]=='2' and s[i-1]<'7'):
            count[i] = count[i] + count[i-2]
        print(count)    
    return count[l]       
                          


         
a = decode('12321')    
print(a)
