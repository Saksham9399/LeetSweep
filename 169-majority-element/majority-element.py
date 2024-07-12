class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_list = {}
        for i in nums:
            if i not in num_list.keys():
                num_list[i] = 1
            else:
                num_list[i] +=1
            if num_list[i] >= len(nums)/2:
                return i
        