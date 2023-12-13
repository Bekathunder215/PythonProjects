import time
import random

def normalsearch(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def binarysearch(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list)-1
    if high < low:
        return -1
    mid = (low + high) // 2
    if list[mid] == target:
        return mid
    elif target < list[mid]:
        return binarysearch(list, target, low, mid-1)
    else:
        return binarysearch(list, target, mid +1, high=high)
    
if __name__ == '__main__':
    length = 20000
    sortedlist = set()
    while len(sortedlist) < length:
        sortedlist.add(random.randint(-3*length, 3*length))
    sortedlist = sorted(list(sortedlist))
    target =10

    start = time.time()
    #this for loop runs the normal search length times..
    for target in sortedlist:
        normalsearch(sortedlist, target)
    end = time.time()
    print("Normal search took: ", (end-start), " seconds")
    print("Average of Normal search per itteration is: ", (end-start)/length, " seconds")
    
    start = time.time()
    #this for loop runs the binary search length times..
    for target in sortedlist:
        binarysearch(sortedlist, target)
    end = time.time()
    print("Binary search took: ", (end-start), " seconds")
    print("Average of Binary search per itteration is: ", (end-start)/length, " seconds")
