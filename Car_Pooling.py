class Solution:
    def carPooling(self, trips,capacity):
        trips.sort(key=lambda x:x[2])
        length = trips[-1][2]

        values = [0]*(length+1)
        prefixsum = [0]
        for trip in trips:
            people,start,end = trip
            values[end]+=-1*people
            values[start] += people
        for i in range(1,len(values)):
            prefixsum = prefixsum + [prefixsum[-1]+values[i]]
            if prefixsum[i]>capacity:
                return False
        return True
