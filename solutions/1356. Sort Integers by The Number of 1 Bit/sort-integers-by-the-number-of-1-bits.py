class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        nums_by_bits = dict()
        max_count = 0
        for num in arr:
            n = num
            count = 0
            while n:
                count += n & 1
                n >>= 1

            if count > max_count:
                max_count = count

            if count not in nums_by_bits:
                nums_by_bits[count] = []

            nums_by_bits[count].append(num)

        for count in nums_by_bits.keys():
            nums_by_bits[count].sort()

        ans = []
        for count in range(max_count + 1):
            if count in nums_by_bits:
                for num in nums_by_bits[count]:
                    ans.append(num)

        return ans
