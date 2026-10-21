class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        value1 = 0
        value2 = 0
        index = 0
        for num in nums:
            if num in freq:
                value1 = index
                value2 = nums.index(freq[num])
            curr = target - num
            freq[curr] = num
            index += 1
        
        return [min(value1, value2),max(value1, value2)]
