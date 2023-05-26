user = int(input("n: "))
list =[]
for i in range(1,int(user)+1):
    if i%3 == 0:
        list.append("Fizz")
        if i% 5 ==0:
            list.append("FizzBuzz")
    elif i%5 == 0:
        list.append("Buzz")
    else:
        list.append(i)
print(list)