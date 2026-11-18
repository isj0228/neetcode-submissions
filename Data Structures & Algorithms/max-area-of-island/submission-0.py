class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1 ,0)]
        visited = [[0] * cols for _ in range(rows)]
        queue = deque()
        count = 0
        def dfs(r, c):
            if visited[r][c] == 1 or grid[r][c] == 0:
                return 0
            visited[r][c] = 1
            area = 1
            for direction in directions:
                cr = r + direction[0]
                cc = c + direction[1]
                if cr >= 0 and cr < rows and cc >= 0 and cc < cols and grid[cr][cc] == 1:
                    area += dfs(cr, cc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current = dfs(r, c)
                    count = max(current, count)
        return count

        
            

