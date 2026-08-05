class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        if not n:
            return 0
        k = 1
        for i in range(1, len(n)):
            if n[i] != n[k - 1]:
                n[k] = n[i]
                k += 1
        return k