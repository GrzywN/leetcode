class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0

        while n:
            sum += n % 10
            product *= n % 10
            n //= 10

        return product - sum
