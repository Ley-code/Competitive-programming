# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

for i in range(int(input())):
  n = int(input())
  val = n%7
  if val==0:
    print(n)
  else:
    num = str(n)
    one,two = n-val,n+(7-val)
    val1 = str(one)
    val2 = str(two)
    ans = ""
    count1 = 0
    for i,c in enumerate(val1):
      if c!=num[i]:
        count1+=1
      if val2[i]!=num[i]:
        count1-=1
    if count1>0:
      print(val2)
    else:
      print(val1)  


        


    
