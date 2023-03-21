class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum = 0
        current_column_primary = 0
        current_column_secondary = len(mat[0]) - 1

        for row in mat:
            if not current_column_primary == current_column_secondary:
                sum += row[current_column_primary]
                sum += row[current_column_secondary]
            else:
                sum += row[current_column_primary]

            current_column_primary += 1
            current_column_secondary -= 1

        return sum
