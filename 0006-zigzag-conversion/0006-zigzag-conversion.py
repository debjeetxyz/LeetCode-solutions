class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        r = [[] for _ in range(numRows)]
        i,d = 0,1
        for char in s:
            r[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d
        for i in range(numRows):
            r[i] = ''.join(r[i])
        return ''.join(r)