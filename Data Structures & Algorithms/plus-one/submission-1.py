class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        additional = 0
        digits[len(digits) - 1] = digits[len(digits) - 1] + 1
        for i in range(len(digits)):
            n = digits[len(digits) - i - 1]
            n = n + additional
            if n == 10:
                additional = 1
            else:
                additional = 0
            digits[len(digits) - i - 1] = n % 10
        if digits[0] == 0:
            array = []
            array.append(1)
            for i in digits:
                array.append(i)
            digits = array
        
        return digits