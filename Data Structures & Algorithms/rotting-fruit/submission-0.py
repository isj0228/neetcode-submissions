from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [ (-1,0), (0,1), (0,-1), (1,0)]
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        minute = 0
        count = len(q)
        while q:
            print(q)
            if count == 0:
                minute += 1
                count = len(q)
            current = q.popleft()
            count -= 1
            for dr, dc in directions:
                nr = current[0] + dr
                nc = current[1] + dc
                if nr >= 0 and nr < rows and nc >=0 and nc < cols and grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append([nr, nc])
        
        if fresh != 0:
            return -1
        return minute
