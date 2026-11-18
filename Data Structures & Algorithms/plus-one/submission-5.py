class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        current = len(digits) - 1
        if digits == [0]:
            return [1]
        while current >= 0 and digits[current] == 9:
            digits[current] = 0
            current -= 1
        if digits[current] == 0 and current ==  -1:
            digits = [1] + digits
        else:
            digits[current] += 1
        return digits