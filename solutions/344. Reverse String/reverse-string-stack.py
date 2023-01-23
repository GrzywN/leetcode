
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        stack = []

        for character in s:
            stack.append(character)

        stack_len = len(stack)

        for i in range(stack_len):
            s[i] = stack.pop()
