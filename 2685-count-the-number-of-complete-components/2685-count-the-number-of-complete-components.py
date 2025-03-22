class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Build adjacency list representation of the graph
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # Step 2: Use DFS to find connected components
        visited = set()
        complete_count = 0

        def dfs(node, component):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    component.add(current)
                    stack.extend(graph[current] - visited)

        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                
                # Step 3: Check completeness condition
                node_count = len(component)
                edge_count = sum(len(graph[node]) for node in component) // 2
                if edge_count == (node_count * (node_count - 1)) // 2:
                    complete_count += 1

        return complete_count
    