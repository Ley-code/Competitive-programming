def isPalindrome(input):
    inputstr = str(input)
    left = 0
    right = len(inputstr)-1
    while left<= right:
        if inputstr[left] != inputstr[right]:
            return False
        left+=1
        right-=1
    return True
print(isPalindrome("121"))