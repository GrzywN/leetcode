class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_and_indexes = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in numbers_and_indexes:
                return [i, numbers_and_indexes[diff]]

            numbers_and_indexes[num] = i
