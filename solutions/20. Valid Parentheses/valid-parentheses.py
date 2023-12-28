from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        matching_brackets = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for letter in s:
            if letter in matching_brackets:
                stack.append(letter)
            elif stack and letter == matching_brackets[stack.pop()]:
                continue
            else:
                return False

        return len(stack) == 0
