class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_nums_sorted = [num * num for num in nums]
        square_nums_sorted.sort()

        return square_nums_sorted
