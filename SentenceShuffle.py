def shuffle():
    s = "is2 sentence4 This1 a3"
    slisted = []
    numbers = []
    splitted =s.split()
    for i in splitted:
        slisted.append(i)
    for substring in slisted:
        numbers.append(substring[-1])
    for j in range(len(numbers)):
        for k in range(len(numbers)-1):
            if int(numbers[j]) > int(numbers[k+1]):
                temp =numbers[j]
                numbers[j] = numbers[k+1]
                numbers[k+1] = temp
        
    print(numbers)
shuffle()
