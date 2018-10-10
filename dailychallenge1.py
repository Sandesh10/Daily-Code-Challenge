##Given a list of numbers and a number k,
##return whether any two numbers from the list add up to k.
##For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def check_list(data, k):
    store = []
    for i in range(0,len(data)):
        temp = k - data[i]
        if temp>=0 and temp in store:
            return True
        else:
            store.append(data[i])
    return False


data = [1,4,45,6,20,-4]
k= 16
print(check_list(data,k))

