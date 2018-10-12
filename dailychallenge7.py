'''
Using Dynamic Programming
'''

def decode(s):
    l = len(s)
    count = [0 for i in range(l+1)]
    count[0] = 1
    count[1] = 1

    for i in range(2,l+1):
##        print(s[i-1])
        if s[i-1]>'0':
            count[i] = count[i-1]
##        print(count)
        if s[i-2]<'2' or (s[i-2]=='2' and s[i-1]<'7'):
            count[i] = count[i] + count[i-2]
##        print(count)    
    return count[l]       
                          
         
print(decode('26123'))    


'''
RECURSIVE SOLUTION


class Solution:
    def numDecodings(self, s):
        
        length = len(s)
        if length==0 or length==1:
            return 1
        
        count = 0
        if s[length-1]>'0':
            count = self.numDecodings(s[:length-1])
        if s[length-2]<'2' or (s[length-2]==2 and s[length-1]<7):
            count += self.numDecodings(s[:length-2])
            
        return count
'''
