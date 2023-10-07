def maxCoins(piles):
    sum = 0
    piles.sort()
    for i in range(-2,(-2*(len(piles)//3))-1,-2):
        sum+=piles[i]
    return sum