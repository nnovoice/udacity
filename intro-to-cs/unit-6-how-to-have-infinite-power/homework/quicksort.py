arr = [123, 1, 98, 78, -1, 0, 765, 8981, 993, 343, 43, -99, 0, -1]
expected = [-99, -1, -1, 0, 0, 1, 43, 78, 98, 123, 343, 765, 993, 8981]

def partition(l):
    print "partition called on ", l, " with len= ", len(l)
    count = len(l)
    pivot = l[0]
    i = 0
    j = count - 1
    while (i < j):
        left = i
        while left <= j:
            if (l[left] > pivot):
                break
            left += 1

        right = j
        while (right >= i):
            if (l[right] < pivot):
                break
            right -= 1

        if (left < right):
            print "left= ", left, " leftVal= ", l[left], " right= ", right, " rightVal= ", l[right]
            l[left], l[right] = l[right], l[left]
        else:
            break

        i = left
        j = right

    print " right= ", right, " rightVal= ", l[right]
    print "left= ", left, " leftVal= ", l[left]
    l[0],l[left] = l[left],l[0]
    print l
    return left

def quicksort(l):
    if len(l) <= 1:
        return
    
    new_pivot_index = partition(l)
    quicksort(l[0:new_pivot_index])
    quicksort(l[new_pivot_index:])

print arr
quicksort(arr)
print arr
if arr == expected:
    print 'All izz well'
else:
    print 'All izz NOT well :-)'
    
