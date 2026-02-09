from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxA = k
        total = 0
        left = 0
        i = k
        count = 0
        for j in range(k):
            if nums[j] == 0:
                count+=1
        while i<len(nums):
            if nums[i] ==0:
                count+=1
                if count>k:
                    while count>k:
                        if nums[left] ==0:
                            count-=1
                        left+=1
            total = i-left+1
            maxA = max(maxA, total)
            i+=1
        return maxA














