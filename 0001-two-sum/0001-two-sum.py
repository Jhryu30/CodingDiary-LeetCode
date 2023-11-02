# [python with alg. 175] 3. save time using dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {num:i for i,num in enumerate(nums)}

        for i,num in enumerate(nums):
            if target-num in nums_map and not i==nums_map[target-num]:
                return nums.index(num), nums_map[target-num]