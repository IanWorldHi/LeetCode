from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = [[False]*len(maze[0]) for i in range(len(maze))]
        depth = 0
        qu = deque([entrance])
        visited[entrance[0]][entrance[1]] = True
        while qu:
            size = len(qu)
            depth+=1
            for i in range(size):
                popped = qu.popleft()
                if (popped[0] == len(maze)-1 or popped[1] == len(maze[0])-1 or popped[1] ==0 or popped[0] == 0) and [popped[0], popped[1]] != entrance:
                    return depth-1
                if popped[0]+1<=len(maze)-1 and maze[popped[0]+1][popped[1]] == '.' and visited[popped[0]+1][popped[1]] == False:
                    qu.append([popped[0]+1, popped[1]])
                    visited[popped[0]+1][popped[1]] = True
                if popped[0]-1>=0 and maze[popped[0]-1][popped[1]] == '.' and visited[popped[0]-1][popped[1]] == False:
                    qu.append([popped[0]-1, popped[1]])
                    visited[popped[0]-1][popped[1]] = True
                if popped[1]+1<=len(maze[0])-1 and maze[popped[0]][popped[1]+1] == '.' and visited[popped[0]][popped[1]+1] == False:
                    qu.append([popped[0], popped[1]+1])
                    visited[popped[0]][popped[1]+1] = True
                if popped[1]-1>=0 and maze[popped[0]][popped[1]-1] == '.'and visited[popped[0]][popped[1]-1] == False:
                    qu.append([popped[0], popped[1]-1])
                    visited[popped[0]][popped[1]-1] = True
        return -1
        




        



        
        

        