class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        neighbors = defaultdict(list)
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)
        
        def dfs(current_node, end_node, visited):
            if current_node == end_node:
                return True
            if current_node in visited:
                return False
            
            visited.add(current_node)
            for neighbor in neighbors[current_node]:
                if dfs(neighbor, end_node, visited):
                    return True
                
            return False
        
        if start == end:
            return True
        
        visited = set()
        return dfs(start, end, visited)
