class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []

        for searched_num in nums1:
            idx = nums2.index(searched_num)
            was_found = False

            for i in range(idx + 1, len(nums2)):
                if nums2[i] > searched_num:
                    ans.append(nums2[i])
                    was_found = True
                    break

            if not was_found:
                ans.append(-1)

        return ans
