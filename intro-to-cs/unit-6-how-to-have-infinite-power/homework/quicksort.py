arr = [123, 1, 98, 78, -1, 0, 765, 8981, 993, 343, 43, -99, 0, -1]
expected = [-99, -1, -1, 0, 0, 1, 43, 78, 98, 123, 343, 765, 993, 8981]

def partition(l, start, end):
    print ""
    print "partition called start= ", start, " end= ", end, "list= ", l[start:end+1]
    pivot = l[start]
    left = start
    right = end
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
        l[start],l[right] = l[right],l[start]
        print l
        return right
    return start



def quicksort(l, start, end):
    if (start >= end):
        return
    
    new_pivot_index = partition(l, start, end)
    quicksort(l, start, new_pivot_index - 1)
    quicksort(l, new_pivot_index + 1, end) 

print arr
quicksort(arr, 0, len(arr) - 1)
print arr
if arr == expected:
    print 'All izz well'
else:
    print 'All izz NOT well :-)'
    
