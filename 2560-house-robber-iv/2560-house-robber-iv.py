class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canPick(limit:int) -> bool:
            count = 0 
            prev_pick = False

            for val in nums:
                if val <= limit and not prev_pick:
                    count += 1
                    prev_pick = True
                    if count >= k:
                        return True
                else:
                    prev_pick  = False
                    
            return False
        
        left, right = min(nums) , max(nums)
        ans = right
        while left <= right :
            mid =(left+right) // 2
            if canPick(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1 

        return ans