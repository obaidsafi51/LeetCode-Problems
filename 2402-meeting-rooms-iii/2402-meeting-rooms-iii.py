class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        ongoing_meetings = []

        meeting_count = [0] * n

        for start, end in meetings:
            duration = end - start

            while ongoing_meetings and ongoing_meetings[0][0] <= start :
                freed_end, freed_room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, freed_room)

            if available_rooms :
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings,(end, room))
            else:
                next_end, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(ongoing_meetings, (next_end + duration, room))
            
            meeting_count[room] += 1

        return meeting_count.index(max(meeting_count))