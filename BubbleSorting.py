def swaping(values):
    count = 0
    for i in range(0,len(values)):
        for j in range(0,(len(values)-1)):
            if values[j] > values[j+1]:
                temp = values[j]
                values[j] = values[j+1]
                values[j+1] = temp
                count +=1
    print(f"Array is sorted in {count} swaps\nFirst element: {values[0]}\nLast Element: {values[len(values)-1]}")
