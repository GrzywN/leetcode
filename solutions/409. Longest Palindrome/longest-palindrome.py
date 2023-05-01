class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters_and_occurrences = dict()

        for letter in s:
            if letter in letters_and_occurrences:
                letters_and_occurrences[letter] += 1
            else:
                letters_and_occurrences[letter] = 1

        length = 0
        can_length_be_odd = False

        for l, o in letters_and_occurrences.items():
            if o % 2 == 1:
                can_length_be_odd = True
                letters_and_occurrences[l] -= 1

        for l, o in letters_and_occurrences.items():
            if o >= 2:
                length += o

        if can_length_be_odd:
            length += 1

        return length
