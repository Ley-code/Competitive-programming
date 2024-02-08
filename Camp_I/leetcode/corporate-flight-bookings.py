class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        totalbookings = [0]*(n)
        accumulate = 0
        for first,last,seats in bookings:
            totalbookings[first-1] += seats
            if last == n:
                continue
            totalbookings[last] -= seats
        for i in range(n):
            accumulate+=totalbookings[i]
            totalbookings[i]=accumulate
        return totalbookings