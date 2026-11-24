class Solution:
    def reverseBits(self, n: int) -> int:
        arr = []
        check = n
        for i in range(32):            
            arr.append(check % 2)
            check //= 2
        answer = 0
        for i in range(32):
            if arr[31 - i] == 1:
                answer += 2 ** i 
        return answer

