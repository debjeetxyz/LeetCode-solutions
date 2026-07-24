class Solution:
    def threeSum(self, n: list[int]) -> list[list[int]]:
        v = len(n)
        e = []
        n.sort()
        for i in range(v):
            if n[i] > 0:
                break
            if i > 0 and n[i] == n[i-1]:
                continue
            l = i + 1
            r = v - 1
            while l < r:
                t = n[i] + n[l] + n[r]
                if t == 0:
                    e.append([n[i], n[l], n[r]])
                    l+=1
                    r-=1
                    while l<r and n[l] == n[l - 1]:
                        l+=1
                    while l<r and n[r] == n[r + 1]:
                        r-=1
                elif t<0:
                    l+=1
                else:
                    r-=1
        return e
