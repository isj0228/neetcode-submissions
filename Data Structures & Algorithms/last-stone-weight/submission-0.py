import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maximum = []
        for num in stones:
            heapq.heappush(maximum, -num)
        
        while len(maximum) > 1:
            first = abs(heapq.heappop(maximum))
            second = abs(heapq.heappop(maximum))
            result = abs(first - second)
            if result > 0:
                heapq.heappush(maximum, -result)
        
        if len(maximum) == 1:
            return abs(maximum[0])
        else:
            return 0
            