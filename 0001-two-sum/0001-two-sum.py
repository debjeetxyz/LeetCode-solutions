class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return
        for i in range(len(nums)):
            j = target - nums[i]
            if j in nums and nums.index(j) != i:
                return [i,nums.index(j)]
