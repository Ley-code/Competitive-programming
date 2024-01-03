class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        start = 0
        end = len(people)-1
        nboats = 0
        while start <=end:
            if (people[start] + people[end]) <= limit:
                start+=1
                end-=1
            else:
                end-=1
            nboats+=1
        return nboats          

        