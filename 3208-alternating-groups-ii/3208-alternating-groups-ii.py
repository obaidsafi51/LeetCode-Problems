class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        # Edge cases
        if k == 1:
            return n  # Every single tile is trivially an alternating block of length 1
        if k > n:
            return 0  # Can't fit a block of length k in a circle of length n
        
        run = 1  # Length of current run of consecutive differing pairs
        count = 0
        
        # We go around the circle "twice" in terms of comparisons
        for i in range(2 * n):
            current_color = colors[i % n]
            next_color = colors[(i + 1) % n]
            
            if current_color != next_color:
                run += 1
            else:
                run = 1
            
            # If we have at least k consecutive differing pairs, 
            # we have found an alternating block of length k ending at index i
            if run >= k:
                start = i - (k - 1)  # start index of this block
                if 0 <= start < n:  # valid start in the circle
                    count += 1
        
        return count