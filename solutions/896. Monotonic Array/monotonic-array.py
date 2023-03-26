class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        asc, dsc = True, True

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                asc = False
            if nums[i - 1] < nums[i]:
                dsc = False

        return asc or dsc