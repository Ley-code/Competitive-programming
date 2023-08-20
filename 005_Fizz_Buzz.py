n = int(input())
for i in range(1):
    if n % 5 == 0:
        if n % 3 == 0:
            print("FizzBuzz")
            break
        else:
            print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print()