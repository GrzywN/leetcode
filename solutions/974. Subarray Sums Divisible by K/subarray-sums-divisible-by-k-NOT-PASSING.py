class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
      arrays_with_sum_of_k = 0
      currentArrayLength = len(nums)

      while currentArrayLength > 0:
        for starting_index in range(1 + len(nums) - currentArrayLength):
          currentArray = []

          for j in range(starting_index, currentArrayLength + starting_index):
            currentArray.append(nums[j])

          if sum(currentArray) % k == 0: arrays_with_sum_of_k += 1

        currentArrayLength -= 1

      return arrays_with_sum_of_k
