class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_occurred = {}

        for item in nums:
            if item in num_occurred:
                return True
            else:
                num_occurred[item] = True

        return False
