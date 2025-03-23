class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Build Graph (Adjacency List)
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Step 2: Dijkstra's Algorithm
        dist = [sys.maxsize] * n   # Distance from 0 to each node
        ways = [0] * n             # Number of ways to reach each node
        dist[0] = 0
        ways[0] = 1
        
        # Min-Heap (Dijkstra's)
        pq = [(0, 0)]  # (time, node)

        while pq:
            time, node = heappop(pq)

            # If this time is already greater than stored shortest, ignore it
            if time > dist[node]:
                continue

            # Step 3: Explore neighbors
            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time

                # Found a **new shorter** path to `neighbor`
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]  # New shortest path count
                    heappush(pq, (new_time, neighbor))

                # Found **another path** with same shortest time
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n-1]