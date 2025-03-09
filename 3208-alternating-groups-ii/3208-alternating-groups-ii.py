class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
    
        # Edge case: if k == 1, every single tile by itself is trivially alternating.
        # So there are n groups (the entire circle).
        if k == 1:
            return n
        
        # If k > n, there can't be a contiguous block of length k in a circle of length n
        # (unless the problem statement implies we can't have k>n, but just in case):
        if k > n:
            return 0
        
        # 1) Double the circle
        extended = colors + colors  # length = 2n
        
        # 2) Build the 'alt' array: alt[i] = 1 if extended[i] != extended[i+1], else 0
        alt = [0] * (2*n - 1)
        for i in range(2*n - 1):
            alt[i] = 1 if extended[i] != extended[i+1] else 0
        
        # 3) Prefix sum of alt
        prefixAlt = [0] * (2*n)
        for i in range(2*n - 1):
            prefixAlt[i+1] = prefixAlt[i] + alt[i]
        # Note: prefixAlt[-1] is prefix sum up to the last element of alt
        
        # 4) Count how many starting indices [0..n-1] yield an alternating block of length k
        count = 0
        for start in range(n):
            end = start + (k - 1)  # this is where we check alt subarray
            if end < 2*n:  # must be within bounds
                # Sum of alt[start.. end-1] = prefixAlt[end] - prefixAlt[start]
                # We want this sum == (k - 1)
                if prefixAlt[end] - prefixAlt[start] == (k - 1):
                    count += 1
            else:
                # If end >= 2n, we can't form a length-k window in the extended array
                # from this start. So break out early.
                break
        return count

        