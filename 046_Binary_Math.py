def binarytonum(binary):
    num = 0
    for i in range(1,len(binary)+1):
        if binary[-i] == "1":
            num+=(2**(i-1))
    return num
def numbertobinary(number):
    binary =''
    while number>0:
        if number %2 == 0:
            binary += "0"
        elif number%2 != 0:
            binary += "1"
        number = number // 2
    return binary[::-1]
num = 0
for i in range(2):
    num+=(binarytonum(input()))
print(numbertobinary(num))