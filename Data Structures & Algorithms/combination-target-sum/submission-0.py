class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        path = []
        self.backtrack(0, nums, answer, path, target)
        return answer
    

    def backtrack(self, index, nums, answer, path, target):
        check = 0
        for i in path:
            check += i
            
        if check == target:
            answer.append(path[:])
            return
        if check > target or index == len(nums):
            return
        path.append(nums[index])
        self.backtrack(index, nums, answer, path, target)

        path.pop()
        self.backtrack(index + 1, nums, answer, path, target)
        