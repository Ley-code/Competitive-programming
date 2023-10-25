'''You are given the sitting arrangement of one row of a class in A2SV as a string called seats. Seats[i] is either ‘E’ meaning it’s empty or ‘T’ meaning it’s taken. 

We want to have at least k people to sit next to each other. In one operation you can have a student take an empty seat. The seat then becomes taken.

Return the minimum number of operations needed such that there are k students sitting next to each other.


Example 1:
Input: seats = "ETTEETTETE", k = 7
Output: 3'''
from collections import Counter
def minimum_operations(seats,k):
    right = k-1
    left = 0
    minimum = len(seats)+1
    hashmap = Counter(seats[:k-1])

    while right<len(seats):
        hashmap[seats[right]]+=1
        if k-hashmap["E"] < minimum:
            minimum = k-hashmap["E"]
        hashmap[seats[left]]-=1
        left+=1
        right+=1
    if minimum==len(seats)+1:
        return 0
    else:
        return minimum
print(minimum_operations("ETTEETTETE",7))
'''Question description
Your friend gave you two phone numbers that you have to call but he informed you that he had made a mistake while typing.  He has also told you that he had tried to correct it using ‘#’.  He inserted a '#' in front of digits he wanted to delete. 

You don’t want to make a call to the same number therefore your task is to check if the numbers are equal. Return true if they are equal and false otherwise.
Example 1:
phonenumber1 = “09#91112344#56” phonenumber2 = “0911123446”

'''
def valid_phone_number(phonenumber1,phonenumber2):
    left, right = 0,0
    while left<len(phonenumber1) and right<len(phonenumber2):
        if phonenumber1[left] == "#":
            left+=2
        print(phonenumber1[left]," ",phonenumber2[right])
        if phonenumber1[left] != phonenumber2[right]:
            return False
        left+=1
        right+=1
    return True
print(valid_phone_number("09#91112344#56","0911123446"))
