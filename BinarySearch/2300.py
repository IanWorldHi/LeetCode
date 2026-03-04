from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        successes = []
        len1 = len(potions)
        potions.sort()
        for i in range(len(spells)):
            place = self.binarySearch(potions, spells[i], success)
            if place == -1:
                successes.append(0)
            else:
                successes.append(len1-place)
        return successes
        
    def binarySearch(self, potions, spell, success) -> int:
        left = 0
        right = len(potions)-1
        while left<=right:  
            mid = (left+right)//2
            if potions[mid]*spell >= success and (mid == 0 or potions[mid-1]*spell < success):
                return mid   
            elif potions[mid]*spell >=success:
                right=mid-1
            elif potions[mid]*spell < success:
                left = mid+1
            else:
                right = mid-1
        return -1
        
        



    