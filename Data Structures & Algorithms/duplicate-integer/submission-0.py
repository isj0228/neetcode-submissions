class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        val = len(nums)
        for i in range(val):
            if nums[i] in a:
                return True
            a.add(nums[i])
        return False