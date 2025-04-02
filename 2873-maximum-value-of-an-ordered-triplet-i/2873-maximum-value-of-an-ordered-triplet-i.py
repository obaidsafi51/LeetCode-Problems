class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3 :
            return 0
        left_max = [0] * n
        left_min = [0] * n
        left_max[0] = nums[0]
        left_min[0] = nums[0]

        for j in range(1,n):
            left_max[j] = max(left_max[j-1], nums[j-1])
            left_min[j] = min(left_min[j-1], nums[j-1])
        right_max = [0] *n
        right_min = [0] *n

        right_max[n-1] = nums[n-1]
        right_min[n-1] = nums[n-1]

        for k in range(n-2, -1, -1):
            right_max[k] = max(right_max[k+1], nums[k+1])
            right_min[k] = min(right_min[k+1], nums[k+1])
        
        max_val = float('-inf')

        for j in range(1 , n-1):
            candidate1 = (left_max[j] - nums[j]) * right_max[j]

            candidate2 = (left_min[j] - nums[j]) * right_min[j]

            max_val = max(max_val, candidate1, candidate2)
        return max(max_val , 0)