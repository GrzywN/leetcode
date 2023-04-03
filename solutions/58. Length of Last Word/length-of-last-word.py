class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_word = s.split(' ')[-1]

        return len(last_word)
