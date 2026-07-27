class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        return sum(i for i,j in seen.items() if j == 1)