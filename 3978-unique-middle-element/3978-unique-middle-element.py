class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        c = 0
        for i in nums:
            if i == nums[len(nums)//2]:
                c+=1
        return c == 1
        # if count method was used then return nums.count(nums[len(nums)//2]) == 1