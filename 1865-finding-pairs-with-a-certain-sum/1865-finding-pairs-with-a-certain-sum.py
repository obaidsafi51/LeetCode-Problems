class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)
        self.freq1 = Counter(nums1)

    def add(self, index: int, val: int) -> None:
        ov = self.nums2[index]
        self.freq2[ov] -= 1
        # nums2[index] += val
        nv = self.nums2[index] + val
        self.freq2[nv] += 1

    def count(self, tot: int) -> int:
        result = 0
        
        # Always iterate over the smaller map
        if len(self.freq1) <= len(self.freq2):
            small_map, large_map = self.freq1, self.freq2
            small_nums = True
        else:
            small_map, large_map = self.freq2, self.freq1
            small_nums = False

        for num, cnt in small_map.items():
            target = tot - num
            if target in large_map:
                result += cnt * large_map[target]
        return result 


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)