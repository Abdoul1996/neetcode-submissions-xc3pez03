class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROW, COL = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islandCounter = 0

        def bfs(r: int, c: int) -> None:
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"  # mark as visited

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc

                    # bounds check
                    if not (0 <= nr < ROW and 0 <= nc < COL):
                        continue
                    # already water / visited
                    if grid[nr][nc] == "0":
                        continue

                    grid[nr][nc] = "0"
                    q.append((nr, nc))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islandCounter += 1

        return islandCounter
