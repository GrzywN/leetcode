class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        pow = 1

        for digit in digits[::-1]:
            num += digit * pow
            pow *= 10

        num += 1
        digits_plus_one = []

        while num > 0:
            digit = num % 10
            num = num // 10
            digits_plus_one.append(digit)

        return digits_plus_one[::-1]
