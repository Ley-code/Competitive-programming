number = int(input())
def leastnumber(n):
    for i in range(2,n):
        if n%i == 0:
            return i
print(leastnumber(number))