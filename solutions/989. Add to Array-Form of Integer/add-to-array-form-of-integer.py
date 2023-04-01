class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        power = 1
        num_as_int = 0

        while len(num) > 0:
            digit = num.pop()
            num_to_add = digit * power
            power *= 10
            num_as_int += num_to_add

        num_as_int += k

        num_as_arr = []

        while num_as_int > 0:
            digit_to_append = num_as_int % 10
            num_as_int //= 10
            num_as_arr.append(digit_to_append)

        return num_as_arr[::-1]
