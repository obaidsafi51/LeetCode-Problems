class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        result = [num for num in nums if num != 0]
        count = len(nums) - len(result)
        result.extend([0]*count)
        return result