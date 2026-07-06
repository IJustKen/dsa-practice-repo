# 2 pointers, keep adjusting the window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        seen = set()  # saves everything ONLY within the window, not outside
        res = 0
        l, r = 0, 0  # both start from the same position

        while r<n:  # right pointer starts moving forward until the end of the list
            if s[r] not in seen:
                seen.add(s[r])  # add to seen nums in the window
            else:  # if the new character is in window already
                while l<r:  # move left pointer until we find the duplicate in the window
                    if s[l] == s[r]:  
                        l += 1  
                        break  # do not remove from seen cuz you just encountered it from right pointer
                    else:
                        seen.remove(s[l])
                        l += 1
            r += 1  # move right pointer
            res = max(r-l, res)  # calculate longest substring
        return res
