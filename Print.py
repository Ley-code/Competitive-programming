if __name__ == '__main__':
    n = int(input())
    m = 1
    o = 1
    while m < n:
        m+=1
        o = (o*(10**(len(str(m)))))+m
    print(o)