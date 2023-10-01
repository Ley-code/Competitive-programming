def reverse(x):   
        lst = []
        for i in str(x):
            lst.append(i)
        x = lst
        
        strs = ""
        for i in x:
            strs+=i
        ans = int(strs)
        if (ans>((2**31)-1)) or ans < (-(2**31)):
            print("executed")
            return 0
        return ans
print(reverse(90000))