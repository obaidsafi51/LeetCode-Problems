class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0,0

        n = len(nums)
        for i in range(n):
            if nums[i] < 0 :
                neg += 1
            elif nums[i] > 0 :
                pos += 1
        return max(pos,neg)