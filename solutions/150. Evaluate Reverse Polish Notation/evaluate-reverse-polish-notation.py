from collections import deque


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                operator = token
                second_operand = stack.pop()
                first_operand = stack.pop()

                result = int(eval(f"{first_operand}{operator}{second_operand}"))
                stack.append(result)
            else:
                stack.append(int(token))

        result = stack.pop()
        return result
