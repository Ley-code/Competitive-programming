def hossamandcombinatorics(array,n):
    array.sort()
    left = 0
    right = n-1
    count_left =array.count(array[left])
    count_right = array.count(array[right])
    pairs = 0 
    for i in range(count_left):
        pairs+=2*count_right
    return pairs
testcase = int(input())
for i in range(testcase):
    n = int(input())
    array = list(map(int,input().split()))
    print(hossamandcombinatorics(array,n))
    

    
