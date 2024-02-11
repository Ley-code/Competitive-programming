for i in range(int(input())):
    n = int(input())
    arr = []
    w = str(input())
    for i in range(n):
        arr.append(int(w[i]))
    count = 0
    hashmap= {0:1}
    runningsum = 0
    for i in range(n):
        runningsum+=arr[i]
        if i+1 - runningsum in hashmap:
            count+=hashmap[i+1 - runningsum]
        hashmap[i+1 - runningsum] = hashmap.get(i+1 - runningsum,0)+1
    print(count)