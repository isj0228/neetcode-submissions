class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in dictionary.items():
            bucket[freq].append(num)
        
        answer = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                answer.append(num)
                
                if len(answer) == k:
                    return answer

            
        return answer