class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {} # num, index

        for i, num in enumerate(nums):
            difference = target - num
            if difference in previousMap:
                return [previousMap[difference], i] # previously found num index, new current index
            previousMap[num] = i # populate map with num, index