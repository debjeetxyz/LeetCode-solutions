class Solution:
    def sortColors(self, n: List[int]) -> None:
        l, m, r = 0, 0, len(n)-1
        while m <= r:
            if n[m] == 0:
                n[l], n[m] = n[m], n[l]
                m+=1
                l+=1
            elif n[m] == 1:
                m+=1
            elif n[m] == 2:
                n[m], n[r] = n[r], n[m]
                r-=1
        