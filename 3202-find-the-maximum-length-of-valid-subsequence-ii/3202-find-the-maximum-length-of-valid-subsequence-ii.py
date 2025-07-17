class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)
                max_len = max(max_len, dp[i][mod] + 1)

        return max_len