class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index in range(len(nums)):
            if target < nums[index]:
                return 0
            if nums[index] == target:
                return index
            if target > nums[index]:
                if (index + 1) < len(nums) and target < nums[index + 1]:
                    return index + 1
                elif (index + 1) == len(nums):
                    return index + 1
