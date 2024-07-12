class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]* len(nums)
        prefix = postfix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]
        for y in range(len(nums)-1,-1,-1):
            result[y] = result[y] * postfix
            postfix = postfix * nums[y]
    
        return result
