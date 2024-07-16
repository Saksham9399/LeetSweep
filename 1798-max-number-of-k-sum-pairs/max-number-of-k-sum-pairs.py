class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        max_operation = 0
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l]+nums[r]==k:
                max_operation+=1
                l+=1
                r-=1
            elif nums[l]+nums[r]<k:
                l+=1
            else:
                r-=1
        return max_operation

        