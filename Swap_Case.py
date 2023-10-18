def swap_case(s):
    swapped = ""
    for i in range(len(s)):
        if 65<=ord(s[i])<=90:
            swapped+= s[i].lower()
        else:
            swapped+= s[i].upper()
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

