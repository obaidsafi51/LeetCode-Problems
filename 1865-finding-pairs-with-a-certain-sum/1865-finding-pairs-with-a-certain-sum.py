class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)
        self.freq1 = Counter(nums1)

    def add(self, index: int, val: int) -> None:
        ov = self.nums2[index]
        self.freq2[ov] -= 1
        if self.freq2[ov] == 0:
            del self.freq2[ov]
        #self.nums2[index] += val
        nv = ov + val
        self.nums2[index] = nv 
        self.freq2[nv] += 1

    def count(self, tot: int) -> int:
        result = 0
        if len(self.freq1) <= len(self.freq2):
            small_map, large_map = self.freq1, self.freq2
        else:
            small_map, large_map = self.freq2, self.freq1
        for num, cnt in small_map.items():
            target = tot - num
            if target in large_map:
                result += cnt * large_map[target]
        return result 

# class FindSumPairs:
#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1 = nums1
#         self.nums2 = nums2
#         self.freq1 = Counter(nums1)
#         self.freq2 = Counter(nums2)

#     def add(self, index: int, val: int) -> None:
#         old_val = self.nums2[index]
#         self.freq2[old_val] -= 1
#         if self.freq2[old_val] == 0:
#             del self.freq2[old_val]

#         new_val = old_val + val
#         self.nums2[index] = new_val
#         self.freq2[new_val] += 1

#     def count(self, tot: int) -> int:
#         result = 0
#         # pick the smaller map for efficiency
#         if len(self.freq1) <= len(self.freq2):
#             small_map, large_map = self.freq1, self.freq2
#         else:
#             small_map, large_map = self.freq2, self.freq1

#         for num, cnt in small_map.items():
#             target = tot - num
#             if target in large_map:
#                 result += cnt * large_map[target]
#         return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)