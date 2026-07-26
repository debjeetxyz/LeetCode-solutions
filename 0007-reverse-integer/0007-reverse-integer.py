class Solution:
    def reverse(self, n: int) -> int:
        s = str(n)
        if n < 0:
            s = s[len(s)-1:0:-1]
            r = -int(s)
        else:
            s = s[::-1]
            r = int(s)
        if r < -2**31 or r > 2**31 - 1:
            return 0
        return r