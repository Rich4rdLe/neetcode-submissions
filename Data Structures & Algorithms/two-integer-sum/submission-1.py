class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {} # num, index

        for i, num in enumerate(nums):
            difference = target - num
            if difference in previousMap:
                return [previousMap[difference], i]
            previousMap[num] = i