import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.kth = []
        for num in nums:
             heapq.heappush(self.kth, num)
        while len(self.kth) > k:
            heapq.heappop(self.kth)

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heappush(self.kth, val)
        while len(self.kth) > self.k:
            heapq.heappop(self.kth)
        return self.kth[0]
