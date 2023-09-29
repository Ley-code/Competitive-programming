def poweroffour(num):
    if num == 1:
        return True
    elif num <= 1:
        return False
    return poweroffour(num//4)
print(poweroffour(64))