class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        prefix_sum = sum(nums[:n])
        prefix_mins = [prefix_sum]

        for i in range(n, 2*n):
            heapq.heappush(max_heap , -nums[i])
            prefix_sum += nums[i]
            prefix_sum += heapq.heappop(max_heap)
            prefix_mins.append(prefix_sum) 

        min_heap = nums[2 * n:]  
        heapq.heapify(min_heap)
        suffix_sum = sum(nums[2 * n:])
        suffix_maxs = [0] * (n + 1)
        suffix_maxs[n] = suffix_sum 


        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            suffix_sum += nums[i]
            suffix_sum -= heapq.heappop(min_heap)
            suffix_maxs[i - n] = suffix_sum

        
        min_diff = float('inf')
        for i in range(n + 1):
            diff = prefix_mins[i] - suffix_maxs[i]
            min_diff = min(min_diff, diff)

        return min_diff