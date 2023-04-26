class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapped_chars = dict()

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in mapped_chars and mapped_chars[s_char] != t_char:
                return False

            mapped_chars[s_char] = t_char

        if len(set(mapped_chars.values())) != len(mapped_chars):
            return False

        return True
