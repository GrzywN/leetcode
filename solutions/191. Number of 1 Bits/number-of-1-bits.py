class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        str_bin_n = bin(n)

        for letter in str_bin_n:
            if letter == '1':
                counter += 1

        return counter
