from collections import defaultdict
#makes default values for the dict keys
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        emptyDict = defaultdict(int)
        for i in grid:
            emptyDict[tuple(i)]+=1
        count = 0
        grid2 = []
        for i in range(len(grid)):
            grid2.append([])
            for j in range(len(grid)):
                grid2[i].append(grid[j][i])
        for i in range(len(grid)):
            count += emptyDict[tuple(grid2[i])]
        return count









