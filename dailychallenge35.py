## Given an array of strictly the characters 'R', 'G', and 'B',
## segregate the values of the array so that all the Rs come first,
## the Gs come second, and the Bs come last.
## You can only swap elements of the array.
##
## Do this in linear time and in-place.
##
## For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
##            it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].



def dailychallenge35(a):
    first =0
    cur = 0
    last = len(a)-1

    while cur<=last:
        if a[cur]=='R':
            a[cur],a[first] = a[first],a[cur]
            first +=1
            cur +=1
        elif a[cur]=='G':
            cur +=1
        else:
            a[cur],a[last]=a[last],a[cur]
            last -=1
    return a


def main():
##    arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    arr = ['R', 'G', 'G', 'R', 'G', 'B', 'G', 'B', 'R', 'R', 'R', 'G']
    result = dailychallenge35(arr)
    print(result)            

if __name__ == '__main__':
    main()
