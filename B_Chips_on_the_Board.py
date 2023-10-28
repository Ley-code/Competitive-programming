def Minimum_cost_of_chips(a,b,n):
    mina = min(a)
    minb = min(b)
    sum1 = (n*mina)+sum(b)
    sum2 = (n*minb)+sum(a)
    print(min(sum1,sum2))
testcase = int(input())
for i in range(testcase):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    Minimum_cost_of_chips(a,b,n)