class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = defaultdict(int)
        heap =[(0, 0, src)]
        graph = defaultdict(list)
        for start, end, dist in flights:
            graph[start].append((dist, end))
        while heap:
            dist, edges, city = heappop(heap)
            if city == dst:
                return dist
            if city in visited and visited[city] <= edges:
                continue
            visited[city] = edges
            if edges > k or city not in graph:
                continue
            for (trip, loc) in graph[city]:
                heappush(heap, (dist + trip, edges + 1, loc))
        return -1 