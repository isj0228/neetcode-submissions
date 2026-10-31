class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        answer = [1, 2]
        for i in range(2, n):
            answer.append(answer[i - 1] + answer[i - 2])
        print(answer)
        return answer[n - 1]