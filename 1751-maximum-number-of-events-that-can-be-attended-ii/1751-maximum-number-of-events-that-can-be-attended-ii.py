class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start time for binary search
        events.sort(key=lambda x: x[0])
        
        # Store only start times for binary search
        start_times = [event[0] for event in events]

        @lru_cache(None)
        def dp(i, remaining):
            if i == len(events) or remaining == 0:
                return 0

            # Option 1: Skip the current event
            skip = dp(i + 1, remaining)

            # Option 2: Take the current event
            # Find the next event that starts after current event ends
            next_index = bisect_left(start_times, events[i][1] + 1)
            take = events[i][2] + dp(next_index, remaining - 1)

            return max(skip, take)

        return dp(0, k)