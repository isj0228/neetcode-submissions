from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:    
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        array = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count = 0
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if nr >=0 and nr < rows and nc >=0 and nc < cols and grid[nr][nc] != 0 and grid[nr][nc] != -1:
                            count += 1
                    if count > 0:
                        array.append([r,c])
        
        q = deque()
        while array:
            treasure = array.pop()
            q.append(treasure)
            check = 1
            flag = 1
            visited = [[0] * cols for _ in range(rows)]
            while q:
                current = q.popleft()
                flag -= 1
                for dr, dc in directions:                    
                    r = current[0] + dr
                    c = current[1] + dc
                    if r >= 0 and r < rows and c >= 0 and c < cols and visited[r][c] == 0 and grid[r][c] != 0 and grid[r][c] != -1 and grid[r][c] != 1:
                        q.append([r, c])
                        visited[r][c] = 1
                        grid[r][c] = min(grid[r][c], check)
                if flag == 0:
                    flag = len(q)
                    check += 1
        
        

            