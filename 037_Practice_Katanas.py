import math
integer = list(map(int,input().split()))
m = integer[0]
n = integer[1]
gcd = math.gcd(m,n)
print((m*n)//gcd)
