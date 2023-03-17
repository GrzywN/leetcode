class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        r = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if not arr[i+1] - arr[i] == r:
                return False

        return True
