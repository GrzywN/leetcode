class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        curr_index = 0

        while left <= right:
            curr_index = int((left + right) / 2)
            curr_val = nums[curr_index]

            if curr_val == target:
                return curr_index
            elif target > curr_val:
                left = curr_index + 1
            else:
                right = curr_index - 1

        return -1
