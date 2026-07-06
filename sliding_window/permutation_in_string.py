# Sliding window yeee
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      
        count = dict()  # keep counts of chars in s1
        for c in s1:
            count[c] = 1 + count.get(c, 0)

        l = 0  # left pointer
      
        curr = dict()  # to store current window's counts
      
        for r in range(len(s2)):
            if s2[r] in count:  # only start counting if the char is in s1 (thus in count)
                curr[s2[r]] = 1 + curr.get(s2[r],0)  # increment
                if curr[s2[r]] > count[s2[r]]:  # if now it exceeds the intended count, 
                    while l < r:  # we iterate left pointer 
                        if s2[l] == s2[r]:  # until we find that character's first occurrence
                            curr[s2[l]] -= 1  # while moving pointer do not forget to decrement existing curr counts
                            l += 1
                            break
                        curr[s2[l]] -= 1  # once more move the pointer to now skip the first occurrence
                        l += 1
                if curr == count:  # wanted case
                    return True
                  
            else:  # this is when the char is not in s1 at all, a discontinuity which means we have to start over
                curr = dict()   # reset curr
                l = r+1  # also now jump the left pointer of the window to the next character

        return False  # not the case
