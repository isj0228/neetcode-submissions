from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:    
        q = deque()

        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            current = q.popleft()
            for dr, dc in directions:
                r = current[0] + dr
                c = current[1] + dc
                if r >= 0 and r < rows and c >= 0 and c <cols and grid[r][c] == INF:
                    q.append([r, c])
                    grid[r][c] = grid[current[0]][current[1]] + 1
