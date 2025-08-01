class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right, val in enumerate(nums):
           
            if val in window:
                return True
            window.add(val)

           
            if right - left == k:
                window.remove(nums[left])
                left += 1

        return False