# BINARY SEARCH
class Solution:
    def _check(self, piles, k):
      # helper function to see how much time it takes to consume all piles at speed k
        time = 0
        for num in piles:
            time += (num + k - 1)//k      # IMPORTANT
            # this is just the ceil of num/k
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # min speed could be anything take 1
    # max would be the max number of bananas in a pile, now do binary search on this speed range
        low = 1
        high = max(piles)
        res = float('inf')

        while low <= high:
            mid = (low+high)//2
            time = self._check(piles, mid)
            if time <= h:  # only update res when we are on time
                res = mid
                high = mid - 1
            elif time > h:
                low = mid + 1
        return res
        
