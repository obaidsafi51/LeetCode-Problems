class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)

        nums1_indices = {num: i for i, num in enumerate(nums1)}

        stack = []

        for cur in nums2:

            while stack and cur > stack[-1]:
                val = stack.pop()

                if val in nums1_indices:
                    ans[nums1_indices[val]] = cur
            stack.append(cur)

        return ans
