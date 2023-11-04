def reading(array1,readingtime):
    array2d = []
    result = ''
    for hours,light in enumerate(array1):
        array2d.append([light,hours+1])
    array2d.sort(key= lambda x:x[0] ,reverse=True)
    for i in range(readingtime):
        result+=(str(array2d[i][1])+" ")
    res.write(str(array2d[readingtime-1][0]))
    res.write('\n')
    res.write(result)
values = open('input.txt','r')
readingtime=int(values.readline().split(' ')[1])
array1 =values.readline().split()
array1=[int(num) for num in array1]
res = open('output.txt','w')
reading(array1,readingtime)