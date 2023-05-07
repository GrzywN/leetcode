class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        new_nums = [None] * (n * 2)

        for i in range(len(nums)):
            new_nums[i] = nums[i]
            new_nums[n + i] = nums[i]

        return new_nums
