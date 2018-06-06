# 二分查找

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left
        # for index in range(len(nums)):
        #     if target < nums[index]:
        #         return 0
        #     if nums[index] == target:
        #         return index
        #     if target > nums[index]:
        #         if (index + 1) < len(nums) and target < nums[index + 1]:
        #             return index + 1
        #         elif (index + 1) == len(nums):
        #             return index + 1
