class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        chars_with_order = dict()
        for i, char in enumerate(order):
            chars_with_order[char] = i

        for i in range(1, len(words)):
            arr1 = words[i - 1]
            arr2 = words[i]

            for j in range(len(arr1)):
                if j > len(arr2) - 1:
                    break

                char_arr_1 = arr1[j]
                char_arr_2 = arr2[j]

                if chars_with_order[char_arr_1] < chars_with_order[char_arr_2]:
                    break
                elif chars_with_order[char_arr_1] > chars_with_order[char_arr_2]:
                    return False
                else:
                    if j == len(arr2) - 1 and len(arr1) > len(arr2):
                        return False

        return True
