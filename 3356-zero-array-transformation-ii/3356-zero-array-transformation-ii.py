from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_zero_with_k(k: int) -> bool:
            """Check if the first k queries can make nums a Zero Array."""
            n = len(nums)
            diff = [0] * (n + 1)  # Difference array
            
            # Apply first k queries using the difference array
            for i in range(k):
                li, ri, vali = queries[i]
                diff[li] -= vali
                if ri + 1 < n:
                    diff[ri + 1] += vali  # Prevent out-of-bounds error
            
            # Apply the difference array to nums
            temp = nums[:]
            curr_decrement = 0
            
            for i in range(n):
                curr_decrement += diff[i]  # Update current decrement
                temp[i] += curr_decrement  # Apply the decrement
                
                if temp[i] > 0:  # If any element is still positive, return False
                    return False
            
            return True  # All elements are zero

        # **Handle edge case:** If nums is already zero, no operations are needed
        if all(num == 0 for num in nums):
            return 0

        # Binary search on k
        left, right = 1, len(queries)
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_zero_with_k(mid):
                result = mid
                right = mid - 1  # Try for a smaller k
            else:
                left = mid + 1  # Increase k to try more queries
        
        return result
