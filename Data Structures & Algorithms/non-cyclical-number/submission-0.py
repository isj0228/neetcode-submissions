class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while True:
            x = []
            while n != 0:
                remain = n % 10
                n = n // 10
                x.append(remain)
            for i in x:
                n += i * i
            
            if n == 1:
                return True
            elif n in check:
                return False
            else:
                check.add(n)


            
