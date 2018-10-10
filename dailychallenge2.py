##Given an array of integers, return a new array such that each element
##at index i of the new array is the product of all the numbers in the
##original array except the one at i.
##
##For example, if our input was [1, 2, 3, 4, 5],
##the expected output would be [120, 60, 40, 30, 24].
##If our input was [3, 2, 1], the expected output would be [2, 3, 6].
##
##Follow-up: what if you can't use division?


def chain_product(data):
    temp =1
    product=[0 for i in range(len(data))]

    for i in range(len(data)):
        product[i] = temp
        temp = temp * data[i]

    temp = 1

    for i in range(len(data)-1,-1,-1):
        product[i]= product[i] * temp
        temp = temp* data[i]

    return product


def main():
    inp = [1, 2, 3, 4, 5]
    print(chain_product(inp))

##Output : [120, 60, 40, 30, 24]

if __name__ == '__main__':
    main()
