class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxSum = 0
        for i in nums:
            if maxSum <0:
                maxSum = 0
            maxSum +=i
            res = max(res,maxSum)
        return res