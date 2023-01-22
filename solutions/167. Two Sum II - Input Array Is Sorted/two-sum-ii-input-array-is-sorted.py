class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1

        while start < end:
            curr_sum = nums[start] + nums[end]

            if curr_sum > target:
                end -= 1
            elif curr_sum < target:
                start += 1
            else:
                return [start + 1, end + 1]
