class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in compliments:
                return [compliments[compliment], i]
            compliments[nums[i]] = i