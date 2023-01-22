class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start = 0

        for end in range(len(nums)):
            if nums[end]:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
