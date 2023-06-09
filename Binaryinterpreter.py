def binarytonumber(binary):
    binary = binary[::-1]
    num = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            num += 2**i     
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


