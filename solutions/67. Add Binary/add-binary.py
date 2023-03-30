class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_bin = int(a, 2)
        b_bin = int(b, 2)

        sum_bin = bin(a_bin + b_bin)
        return str(sum_bin)[2:]
