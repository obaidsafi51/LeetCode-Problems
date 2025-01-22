class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0

        for e in nums:
            if val != e:
                nums[k] = e
                k += 1
        return k