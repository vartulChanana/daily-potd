from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_rooms = list(range(n))
        heapify(available_rooms)
        ongoing_meetings = []
        room_meeting_count = [0] * n

        for start, end in meetings:
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                finished_end, finished_room = heappop(ongoing_meetings)
                heappush(available_rooms, finished_room)

            if available_rooms:
                room = heappop(available_rooms)
                heappush(ongoing_meetings, (end, room))
            else:
                earliest_end, room = heappop(ongoing_meetings)
                delayed_end = earliest_end + (end - start)
                heappush(ongoing_meetings, (delayed_end, room))

            room_meeting_count[room] += 1

        max_meetings = max(room_meeting_count)
        for i in range(n):
            if room_meeting_count[i] == max_meetings:
                return i
