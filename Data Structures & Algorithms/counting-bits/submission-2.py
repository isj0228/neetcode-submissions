class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n + 1)
        answer[0] = 0
        if n == 0:
            return [0]
        answer[1] = 1
        for i in range(2, n + 1):
            answer[i] = answer[i >> 1] + answer[i & 1]
        return answer

