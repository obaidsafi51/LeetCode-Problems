class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()

        left = 0
        max_score = 0
        cur_sum = 0
        
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left += 1 
            seen.add(nums[right])
            cur_sum += nums[right]
            max_score = max(max_score, cur_sum)
        return max_score