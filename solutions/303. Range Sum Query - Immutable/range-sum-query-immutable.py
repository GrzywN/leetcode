class NumArray:

    def __init__(self, nums: list[int]):
        self.prefixes = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            self.prefixes.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefixes[right]
        left_sum = self.prefixes[left - 1] if left > 0 else 0

        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
