from itertools import chain


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        needed_matrix_length = r * c
        flatten_matrix = list(chain(*mat))
        reshaped_matrix = []

        if not len(flatten_matrix) == needed_matrix_length:
            return mat

        curr_index = 0
        for row in range(r):
            row_to_append = []
            for _ in range(c):
                row_to_append.append(flatten_matrix[curr_index])
                curr_index += 1

            reshaped_matrix.append(row_to_append)

        return reshaped_matrix
