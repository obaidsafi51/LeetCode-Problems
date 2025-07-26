class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        pairs = [(a, b, i) for i, (a, b) in enumerate(conflictingPairs)]
        pairs.sort(key=lambda x: x[1])

        heap = []
        L   = [0] * (n + 1)  
        L2  = [0] * (n + 1)  
        contrib = [None] * (n + 1)  
        i = 0 
        m = len(pairs)
        for r in range(1, n + 1):
           
            while i < m and pairs[i][1] <= r:
                a, b, idx = pairs[i]
                heapq.heappush(heap, (-a, idx))
                i += 1

            if heap:
                tops = heapq.nsmallest(2, heap) 
                top1_a, top1_idx = -tops[0][0], tops[0][1]
                top2_a = -tops[1][0] if len(tops) > 1 else 0
            else:
                top1_a, top1_idx, top2_a = 0, None, 0

            L[r]       = top1_a
            L2[r]      = top2_a
            contrib[r] = top1_idx

        G0 = sum(r - L[r] for r in range(1, n + 1))

        gain = defaultdict(int)
        for r in range(1, n + 1):
            p = contrib[r]
            if p is not None:
                gain[p] += (L[r] - L2[r])

        best_gain = max(gain.values(), default=0)

        return G0 + best_gain
