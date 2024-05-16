class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmaps
        pair_map = {}
        for idx, num in enumerate(nums):
            if (target -num) in pair_map.keys():
                return [idx,pair_map[target-num]]
            pair_map[num] = idx

        