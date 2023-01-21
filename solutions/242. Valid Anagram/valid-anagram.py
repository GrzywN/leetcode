class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_occurred = {}

        for letter in s:
            if letter in letter_occurred:
                letter_occurred[letter] += 1
            else:
                letter_occurred[letter] = 1

        for letter in t:
            if letter in letter_occurred and letter_occurred[letter] == 0:
                return False

            if letter in letter_occurred:
                letter_occurred[letter] -= 1
            else:
                return False

        return True
