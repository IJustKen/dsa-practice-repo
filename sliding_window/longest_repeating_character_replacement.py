# approach O(26.n)
# Essentially for any window, we need to see the character with the maximum frequency. Rest all can be replaced according to the question.
# Thus the (window size - highest frequency) will give the impurity of the window, which should be <= k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()  # maintain counts of each character in the window
        res = 0  # final result of longest repeating characters
        l = 0  # left pointer
        for r in range(len(s)):  # keep moving right pointer
            count[s[r]] = 1 + count.get(s[r], 0)

            # notice each time we do a max() it is O(26)
            while (r-l+1) - max(count.values()) > k:  # but if impurity is more, start moving left pointer until impurity goes away
                count[s[l]] = max(count.get(s[l], 0) - 1, 0)  # do not forget to decrement the count
                l += 1
            # after the above two steps, we now have a valid window with impurity under control
            res = max(res, r-l+1)  # then calculate the length of this valid window

        return res

# Approach [OPTIMAL]: O(n), do not have to do max(count.values())
# window_size - max_f <= k is the condition. If you increase max_f here, window_size will also have to increase which means maximizing window_size is
# depending only on max_f. If currently max_f is of 'A' as 4 but it decrements to 2 and now 'B' has max_f of 3, does not matter, max_f is still 4. Because for
# the condition to hold, window size would have been max when max_f was its highest.
# Thus only keep track of max_f seen so far, and update on the way if you get greater max_f
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        res = 0
        l = 0
        max_f = 0  # maintain this
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])

            while (r-l+1) - max_f > k:  # keep comparing with the biggest max_f seen till now
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res
