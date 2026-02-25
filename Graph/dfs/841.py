from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        visited = self.dfs(rooms, visited, 0)
        if False in visited:
            return False
        return True
    def dfs(self, rooms: List[List[int]], visited: List[bool], visiting: int) -> List[bool]:
        if visited[visiting] == True:
            return []
        visited[visiting] = True
        for i in range(len(rooms[visiting])):
            self.dfs(rooms, visited, rooms[visiting][i])
        return visited
        
        


        
        



        