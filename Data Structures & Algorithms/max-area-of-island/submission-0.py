from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
              
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            area = 0 
              
            while q:
                row, col = q.popleft()
                area += 1

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):

                        visited.add((nr, nc))
                        q.append((nr, nc))

            return area
       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea




        # Input as grid 
        # output : Maximum area of Island which means the highest connectivity island 

        # Constrain: 
        # 1 <= grid.length, grid[i].length <=50  == row x 50 , col x 50 
        # Total Cells = 2500 in totoal of the grid 
        # Tc : O (row, col) each cell is O(1) and we only visiting once 
        # Sc : O(row, col) is the worse case which means the entire grid has 1s 

        # Plan: 
            # 1. using BFS bc I'll be visiting each cell and which means rows x cols
            # 2. Data structure : Queue 

        # Pseudocode: 
            # 1. Handle base cases 
            # 2. build bfs function
                # ititialize Q and maxIsland  
                # handle adjacent direction(up, down, left, right)
                # call for loop that iterate grid 
                # check if cell has 1 and not visited then add to the que and visited right after 
            # 3. iterate through entire grid 
                    # call bfs 
                    # return max Island
                    

        