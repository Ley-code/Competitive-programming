# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E


for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    presum = [0]
    for i in range(n):
        presum.append(presum[-1]+nums[i])

    for q in range(int(input())):
        left, u = map(int, input().split())
        l = left-1
        r = len(presum) - 1
        while left < r:
            mid = (left+r + 1) // 2
            if presum[mid] <= u+presum[l]:
                left = mid 
            else:
                r = mid - 1 

        if left + 1 < len(presum) and abs(presum[left] - (u + presum[l])) > abs(presum[left + 1] - (u+presum[l]))-1:
            left += 1
        print(left, end=" ")
    print()
         