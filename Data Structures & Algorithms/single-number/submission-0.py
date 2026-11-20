class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = set()
        for num in nums:
            if num not in check:
                check.add(num)
            else:
                check.remove(num)
        
        return check.pop()