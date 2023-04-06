class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # Save top left value
                saved_top_left = matrix[top][left + i]

                # Swap 3 values
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]

                # Override saved original top left value
                matrix[top + i][right] = saved_top_left

            left += 1
            right -= 1
