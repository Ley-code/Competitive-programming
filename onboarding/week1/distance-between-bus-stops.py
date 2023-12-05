class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        totaldistance = sum(distance)
        if start<destination:
            forward = sum(distance[start:destination])
            backward = totaldistance - forward
            return min(forward,backward)
        elif start>destination:
            backward = sum(distance[destination:start])
            forward = totaldistance - backward
            return min(backward,forward)
        else:
            return 0

