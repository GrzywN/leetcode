class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters_s = dict()
        letters_t = dict()

        for letter in s:
            if letter in letters_s:
                letters_s[letter] += 1
            else:
                letters_s[letter] = 1

        for letter in t:
            if letter in letters_t:
                letters_t[letter] += 1
            else:
                letters_t[letter] = 1

        for k, v in letters_t.items():
            if k not in letters_s or letters_s[k] < letters_t[k]:
                return k

        return ""
