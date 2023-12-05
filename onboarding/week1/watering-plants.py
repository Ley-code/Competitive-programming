class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        totalsteps = 0
        temp = capacity
        for i in range(len(plants)):
            if plants[i]<=temp:
                totalsteps+=1
                temp-=plants[i]
            elif plants[i]>temp:
                totalsteps+=(i+1)+(i)
                temp = capacity-plants[i]
        return totalsteps