class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_num = nums[0]

        max_consecutive_ones = prev_num
        cur_consecutive_ones = prev_num

        for i in range(1, len(nums)):
            if nums[i] and nums[i] == prev_num:
                cur_consecutive_ones += 1
            elif nums[i]:
                cur_consecutive_ones = 1
            else:
                cur_consecutive_ones = 0

            if cur_consecutive_ones > max_consecutive_ones:
                max_consecutive_ones = cur_consecutive_ones

            prev_num = nums[i]

        return max_consecutive_ones
