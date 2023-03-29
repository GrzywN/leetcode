class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                result[i1 + i2] += digit
                result[i1 + i2 + 1] += result[i1 + i2] // 10
                result[i1 + i2] = result[i1 + i2] % 10

        result = result[::-1]
        beg_pointer = 0

        for num in result:
            if int(num) == 0:
                beg_pointer += 1
            else:
                break

        result = map(str, result[beg_pointer:])
        return "".join(result)
