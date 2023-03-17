class Solution:
    def arraySign(self, nums: list[int]) -> int:
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0

        product = 1
        for item in nums:
            product *= item

        return signFunc(product)
