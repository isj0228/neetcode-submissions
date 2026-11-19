from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        queue = deque()
        if node is None:
            return None
        queue.append(node)
        while queue:
            current = queue.popleft()
            if current not in visited:
                new_node = Node(current.val, [])
                visited[current] = new_node
                for neighbor in current.neighbors:
                    queue.append(neighbor)
        for key in visited:
            print(key.val)

        for key in visited:
            for neighbor in key.neighbors:
                visited[key].neighbors.append(visited[neighbor])
        
        return visited[node]


