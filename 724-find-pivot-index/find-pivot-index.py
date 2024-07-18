class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            prefix= sum(nums[:idx])
            postfix= sum(nums[idx+1:])
            if prefix == postfix:
                return idx
        return -1
        