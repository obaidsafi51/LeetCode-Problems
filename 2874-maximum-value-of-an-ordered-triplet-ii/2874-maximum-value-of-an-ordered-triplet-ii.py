from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Step 1: Compute left_max where left_max[j] stores max(nums[0] ... nums[j-1])
        left_max = [0] * n
        left_max[0] = nums[0]
        for j in range(1, n):
            left_max[j] = max(left_max[j-1], nums[j-1])
        
        # Step 2: Compute right_max where right_max[k] stores max(nums[k+1] ... nums[n-1])
        right_max = [0] * n
        right_max[n-1] = nums[n-1]
        for k in range(n-2, -1, -1):
            right_max[k] = max(right_max[k+1], nums[k+1])
        
        # Step 3: Iterate over possible middle index j and compute max value
        max_val = float('-inf')
        for j in range(1, n-1):  # j is the middle element
            if left_max[j] > nums[j] and right_max[j] > 0:
                max_val = max(max_val, (left_max[j] - nums[j]) * right_max[j])

        return max(max_val, 0)  # Ensure we return non-negative result
