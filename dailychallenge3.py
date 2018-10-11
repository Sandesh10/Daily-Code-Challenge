a = [0,1, -1, -5, -3, 3, 4, 2, 8]
l = 0
count=0
for i in range(len(a)):
    if a[i]<=0:
##        print(a[i],a[l], l)
        a[l],a[i] = a[i],a[l]
        l = l+1
        count+=1
mini=1
for i in range(count,len(a)):
    print(a[i])
    if a[i]==mini:
        mini = mini+1
    if a[i]<mini:
        break    

print(mini)        
        
