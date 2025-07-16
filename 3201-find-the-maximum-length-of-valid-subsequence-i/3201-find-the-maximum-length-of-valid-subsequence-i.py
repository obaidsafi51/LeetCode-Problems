class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_even = 0
        count_odd = 0
        max_end_with_even = 0
        max_end_with_odd = 0
        
        for num in nums:
            parity = num % 2
            if parity == 0: 
                dp_i = max_end_with_odd + 1
                max_end_with_even = max(max_end_with_even, dp_i)
                count_even += 1
            else: 
                dp_i = max_end_with_even + 1
                max_end_with_odd = max(max_end_with_odd, dp_i)
                count_odd += 1
        
        longest_alternating = max(max_end_with_even, max_end_with_odd)
        return max(count_even, count_odd, longest_alternating)