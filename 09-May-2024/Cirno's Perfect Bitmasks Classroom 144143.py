# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for i in range(int(input())):
    x = int(input())
    bitcount = 0
    flag = True
    flag2 = True
    y = 0
    firstzero = None
    for i in range(33):
        if (1<<i)&x>0:
            if flag:
                y |= 1<<i
                flag = False
            bitcount+=1
        else:
            if flag2:
                firstzero = i
                flag2 = False
    if bitcount>1:
        print(y)
    else:
        print(y^(1<<firstzero))
            
