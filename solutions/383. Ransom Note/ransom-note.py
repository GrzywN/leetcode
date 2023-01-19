class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_in_magazine = {}

        for letter in magazine:
            letters_in_magazine[letter] = letters_in_magazine.setdefault(letter, 0) + 1

        for letter in ransomNote:
            if letter not in letters_in_magazine or letters_in_magazine[letter] == 0:
                return False

            letters_in_magazine[letter] -= 1

        return True
