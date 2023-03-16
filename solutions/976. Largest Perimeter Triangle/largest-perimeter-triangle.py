class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        a, b = len(nums) - 3, len(nums)

        for i in range(len(nums) - 2):
            triangle = nums[a:b]
            if triangle[0] + triangle[1] > triangle[2]:
                return sum(triangle)

            a -= 1
            b -= 1

        return 0
