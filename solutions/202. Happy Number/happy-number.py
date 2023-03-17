class Solution:
    def isHappy(self, n: int) -> bool:
        current_sum = self.sumOfSquaredNumbers(n)
        all_sums = set()

        while True:
            if current_sum in all_sums:
                return False

            if current_sum == 1:
                return True

            all_sums.add(current_sum)
            current_sum = self.sumOfSquaredNumbers(current_sum)

    def sumOfSquaredNumbers(self, n: int) -> int:
        n_str = str(n)
        current_sum = 0

        for letter in n_str:
            current_sum += int(letter) ** 2

        return current_sum
