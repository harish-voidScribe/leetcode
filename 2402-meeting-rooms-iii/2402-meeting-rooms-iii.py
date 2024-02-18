class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0] * n
        avail = [i for i in range(n)]
        used = []
        meetings.sort()
        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(avail, room)
            if not avail:
                time, room = heappop(used)
                heappush(used, (time + (end - start), room))
            else:
                room = heappop(avail)
                heappush(used, (end, room))
            rooms[room] += 1
        res = 0  
        for i in range(1, len(rooms)):
            if rooms[i] > rooms[res]:
                res = i
        return res