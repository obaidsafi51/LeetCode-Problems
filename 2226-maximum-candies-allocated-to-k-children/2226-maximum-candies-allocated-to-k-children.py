class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        left, right = 1, sum(candies) // k
        best = 0

        def canDistribute(X):
            total = sum(c//X for c in candies)
            return total >= k

        while left <= right :
            mid = (left + right) // 2

            if canDistribute(mid):
                best = mid 
                left = mid +1 
            else:
                right = mid - 1
        return best  