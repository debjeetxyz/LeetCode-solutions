class Solution:
    def firstUniqueEven(self, n: list[int]) -> int:
        seen = []
        for i in range(len(n)):
            if n[i] % 2 == 0 and n.count(n[i]) == 1:
                seen.append(n[i])
        if len(seen) == 0:
            return -1
        if seen:
            return seen[0]