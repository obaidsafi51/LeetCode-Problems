class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        xor = [0] * n
        tin = [0] * n
        tout = [0] * n
        time = 1

        def dfs(u, parent):
            nonlocal time
            tin[u] = time
            time += 1
            xor[u] = nums[u]
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)
                xor[u] ^= xor[v]
            tout[u] = time

        dfs(0, -1)
        total = xor[0]
        res = float("inf")

        for i in range(n):
            for j in range(i + 1, n):
                if i == 0 or j == 0:
                    continue

                def is_child(u, v):
                    return tin[v] <= tin[u] < tout[v]

                if is_child(i, j):
                    xor1 = xor[i]
                    xor2 = xor[j] ^ xor[i]
                    xor3 = total ^ xor[j]
                elif is_child(j, i):
                    xor1 = xor[j]
                    xor2 = xor[i] ^ xor[j]
                    xor3 = total ^ xor[i]
                else:
                    xor1 = xor[i]
                    xor2 = xor[j]
                    xor3 = total ^ xor[i] ^ xor[j]

                res = min(res, max(xor1, xor2, xor3) - min(xor1, xor2, xor3))

        return res