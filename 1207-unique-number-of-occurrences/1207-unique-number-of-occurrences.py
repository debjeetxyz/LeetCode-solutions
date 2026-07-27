class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}
        for i in arr:
            seen[i] = seen.get(i,0) + 1
        counts = list(seen.values())
        return len(counts) == len(set(counts))
