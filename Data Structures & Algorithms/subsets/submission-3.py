class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        path = []
        self.backtrack(0, path, nums, answer)

        return answer
    
    def backtrack(self, index, path, nums, answer):

        if index == len(nums):
            answer.append(path[:])
            return
        
        # choose the current index
        path.append(nums[index])
        self.backtrack(index + 1, path, nums, answer)

        path.pop()
        self.backtrack(index + 1, path, nums,  answer)
        

        