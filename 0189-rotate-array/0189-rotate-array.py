class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(num,l,r):
            while l<r:
                num[l],num[r] = num[r],num[l]
                l+=1
                r-=1
        n = len(nums)
        if k >= n:
            k%=n
        if n>=2:
            reverse(nums,0,n-1)
            reverse(nums,0,k-1)
            reverse(nums,k,n-1)
            