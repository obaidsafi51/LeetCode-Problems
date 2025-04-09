from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        distinct = set()

        for x in nums:
            if x < k:
                return -1 
            
            if x > k:
                distinct.add(x)

        return len(distinct)