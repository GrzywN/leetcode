class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        numbers = []
        while x > 0:
            numbers.append(x % 10)
            x //= 10

        for i in range(len(numbers) // 2):
            if numbers[i] != numbers[len(numbers) - 1 - i]:
                return False

        return True
        # or
        # return str(x) == str(x)[::-1]
