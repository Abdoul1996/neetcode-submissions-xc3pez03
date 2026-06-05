class Solution:
    import math 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        

        while l < r:

            mid = l + (r-l) // 2 

            totalTime = 0 

            totalTime = sum(math.ceil(p/mid) for p in piles)

            if totalTime <= h:
                r = mid  
            else:
                l = mid + 1 
        return l 

        