class Solution:
    def toLowerCase(self, s: str) -> str:
        letters = []

        for letter in s:
            if ord(letter) >= 65 and ord(letter) <= 90:
                letters.append(chr(ord(letter) + 32))
            else:
                letters.append(letter)

        return "".join(letters)
