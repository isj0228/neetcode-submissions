class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = 0
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
            n = max(n, dictionary[num])
        
        bucket = [[] for _ in range(n)]
        for key in dictionary:
            bucket[dictionary[key] - 1].append(key)
        answer = []
        i = 0
        while k > 0:
            if bucket[n- i - 1]:
                for item in bucket[n - i - 1]:
                    if k <= 0:
                        break
                    answer.append(item)
                    k -= 1
                
            i += 1
        return answer