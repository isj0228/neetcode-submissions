class Solution:
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)  # vertical
        cols = len(grid[0])  # horizontal
        island = 0

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    island += 1
                    self.dfs(r, c, grid, visited)

        return island
    def dfs(self, r, c, grid, visited):
        rows = len(grid)
        cols = len(grid[0])
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        # return if its already visited or its water
        if visited[r][c] or grid[r][c] == '0':
            return

        visited[r][c] = True
        for dr, dc in self.directions:
            self.dfs(r + dr, c + dc, grid, visited)