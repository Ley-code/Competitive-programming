testcase = int(input())
for i in range(testcase):
    length = int(input())
    array = []
    response = []
    quality = []
    for j in range(length):
        array = list(map(int,input().split()))
        response.append(array[0])
        quality.append(array[1])
    for i in range(len(response)):
        if response[i]>10:
            quality[i] = 0
    maxindex = quality.index(max(quality))
    print(maxindex+1)
        
