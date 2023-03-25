class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        odd_length_subarrays_sum = 0
        left_ptr = 0
        right_ptr = 1
        current_subarray_length = 1

        while True:
            if current_subarray_length > len(arr):
                break

            curr_subarray = arr[left_ptr:right_ptr]
            odd_length_subarrays_sum += sum(curr_subarray)

            if right_ptr <= len(arr) - 1:
                left_ptr += 1
                right_ptr += 1
            else:
                current_subarray_length += 2
                left_ptr = 0
                right_ptr = current_subarray_length

        return odd_length_subarrays_sum
