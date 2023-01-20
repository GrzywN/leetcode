class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pointer_start = 0
        pointer_end = len(nums) - 1

        while pointer_start <= pointer_end:
            if abs(nums[pointer_end]) < abs(nums[pointer_start]):
                num_to_insert = nums[pointer_start]
                index_to_insert = pointer_end

                del nums[pointer_start]
                nums.insert(index_to_insert, num_to_insert)

            nums[pointer_end] **= 2
            pointer_end -= 1

        return nums
