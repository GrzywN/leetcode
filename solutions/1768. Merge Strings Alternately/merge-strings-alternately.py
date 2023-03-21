class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        letters = []
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i <= len(word1) - 1:
                letters.append(word1[i])
            if i <= len(word2) - 1:
                letters.append(word2[i])

        return "".join(letters)
