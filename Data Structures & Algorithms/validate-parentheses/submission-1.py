class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)

            if char == ')':
                if not stack:
                    return False
                check = stack.pop()
                if check == '(':
                    continue
                else:
                    return False
            if char == ']':
                if not stack:
                    return False
                check = stack.pop()
                if check == '[':
                    continue
                else:
                    return False
            if char == '}':
                if not stack:
                    return False
                check = stack.pop()
                if check == '{':
                    continue
                else:
                    return False
        if not stack:
            return True
        return False
