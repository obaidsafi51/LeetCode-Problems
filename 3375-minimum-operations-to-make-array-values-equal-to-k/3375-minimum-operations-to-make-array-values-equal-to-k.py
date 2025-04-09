class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for x in nums:
            if x < k:
                return -1
        
        if all(x == k for x in nums) :
            return 0
        
        distinct = set(nums)

        op = sum(1 for x in distinct if x > k)

        return op