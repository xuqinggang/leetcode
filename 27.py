class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif val not in nums:
            return len(nums)
        else:
            while val in nums:
                nums.remove(val)
            return len(nums)


print Solution().removeElement([0, 1, 1, 2], 1)
