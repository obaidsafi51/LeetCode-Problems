class Solution:
    def findLHS(self, nums: List[int]) -> int:

        max_len = 0 
        freq = Counter(nums)

        for num in freq:
            if num+1 in freq:
                max_len = max(max_len, freq[num] + freq[num+1])
        return max_len        