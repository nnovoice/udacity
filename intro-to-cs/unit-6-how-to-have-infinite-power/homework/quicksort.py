arr = [123, 1, 98, 78, -1, 0, 765, 8981, 993, 343, 43, -99, 0, -1]
expected = [-99, -1, -1, 0, 0, 1, 43, 78, 98, 123, 343, 765, 993, 8981]

def partition(l):
    print "partition called on ", l, " with len= ", len(l)
    count = len(l)
    pivot = l[0]
    left = 0
    right = count - 1
    print "ENTRY: left= ", left, " leftVal= ", l[left], " right= ", right, " rightVal= ", l[right]
    while (left < right):
        while (l[left] <= pivot):
            left += 1

        while (l[right] > pivot):
            right -= 1

        if (left < right):
            #print "SWAP: left= ", left, " leftVal= ", l[left], " right= ", right, " rightVal= ", l[right]
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    print "OUTSIDE: left= ", left, " leftVal= ", l[left], " right= ", right, " rightVal= ", l[right]

    if (pivot > l[right]):
        l[0],l[right] = l[right],l[0]
        print l
        return right
    return 0



def quicksort(l):
    if len(l) <= 1:
        return
    
    new_pivot_index = partition(l)
    quicksort(l[0:new_pivot_index])
    quicksort(l[new_pivot_index + 1:]) 

print arr
quicksort(arr)
print arr
if arr == expected:
    print 'All izz well'
else:
    print 'All izz NOT well :-)'
    
