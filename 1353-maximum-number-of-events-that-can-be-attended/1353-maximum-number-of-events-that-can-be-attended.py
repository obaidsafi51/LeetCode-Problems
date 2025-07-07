class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap = []
        day = 1
        i = 0
        attended = 0
        n = len(events)

        last_day = max(end for _,end in events)

        while day <= last_day:
            while i < n and events[i][0] == day :
                heappush(min_heap, events[i][1])
                i+=1
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
            
            if min_heap :
                heappop(min_heap)
                attended += 1
            
            day += 1
        return attended 
            