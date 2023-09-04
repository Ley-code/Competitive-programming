number = int(input())
def divisibel57(number):
    if number%5 == 0:
        if number%7 == 0:
            return "YES"
    return "NO"
print(divisibel57(number))