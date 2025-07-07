#Given a string s, find the length of the longest substring without duplicate characters.

class Solution:

  #2 pointer stuff lesgoo
  
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:    #edge case
            return 0
        if len(s) == 1:    #edge case
            return 1
        seen = set()      #to maintain a record of seen chars
        l = 0
        seen.add(s[l])  #we start w 2 pointers one at 0 the other at 1, assuming we have seen 0th already
        r = 1
        maxlen = 1
        while r<len(s):
            if s[r] in seen:
                while s[l] != s[r] and l<r:    #increment l until s[l] == s[r]
                  #s[r] is the char that repeated its last occurrence we are finding
                    seen.remove(s[l])    #v imp to remove the chars we are removing out of this window
                    l += 1
                #now we have the last occurrence idx, so we do l += 1 and r += 1
                l += 1
                r += 1     
            else:      #other case to extend window
                seen.add(s[r])
                r += 1
            maxlen = max(maxlen,r-l)      #step to record max
        return maxlen


        
