class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # for i in range(1, len(s) // 2 + 1):
        #     substring = "".join(s[:i])

        #     if s == substring * (len(s) // len(substring)):
        #         return True

        # return False

        return s in (s+s)[1:-1]
