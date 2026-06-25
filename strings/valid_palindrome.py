# KEY TAKEAWAY: the function for strings .isalnum() checks for alphanumeric characters p fast
# no need to make a wanted set of alpha numeric characters manually
# do not make the inner loops run even when outer loop condition does not match (l<r) thus 
# that condition was added to inner loop as well to avoid CPU overhead
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l<r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
        
