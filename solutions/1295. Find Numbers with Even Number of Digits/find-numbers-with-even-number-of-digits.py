class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_numbers = 0

        for num in nums:
            digits = 1
            while num >= 10:
                num //= 10
                digits += 1

            if digits % 2 == 0:
                even_digit_numbers += 1

        return even_digit_numbers
