class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        how_many_iters = len(haystack) - needle_len + 1

        for i in range(how_many_iters):
            substring = haystack[i:needle_len+i]

            if substring == needle:
                return i

        return -1
