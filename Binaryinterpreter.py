def binarytonumber(binary):
    binary = binary[::-1]
    num = 0

    for i in range(len(binary)):
        if binary[i] == "1":
            num += 2**i
        else:
            num+=0     
    return num


print(binarytonumber("1010101010111"))
