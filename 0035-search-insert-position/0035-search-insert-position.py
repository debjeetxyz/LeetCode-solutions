class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        nums.append(target)
        nums.sort()
        return nums.index(target)