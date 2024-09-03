class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = 0
        for i in range(len(s)):
            num = ord(s[i]) - ord('a') + 1
            while num > 0:
                total += num % 10
                num //= 10
        
        k -= 1
        while k > 0:
            new = 0
            while total > 0:
                new += total % 10
                total //= 10
            total = new
            k -= 1
        
        return total
