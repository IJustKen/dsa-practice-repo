class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = dict()  # get counts of each character in t
        for c in t:
            counts[c] = 1+counts.get(c,0)

        res = None  # normally I would store the result string, but now my plan is to store the result indices, you will see why
        minlen = float("inf")  # length of minimum substring

        to_match = len(counts)  # elements left to match in the window
        temp = dict()  # tracks counts of elements from t present in the current window
        l = 0  # left pointer

        for r in range(len(s)):  # right pointer keeps moving
            curr = s[r]  
            if curr in counts:
                temp[curr] = 1 + temp.get(curr, 0)
                if counts[curr] == temp[curr]:  # match found, decrement to_match
                    to_match -= 1

            while to_match == 0:  # when all characters are matches, start shrinking window with left pointer
                if (r-l+1) < minlen:
                    minlen = r-l+1
                    res = (l,r)  # store l and r indices because s[l:r+1] is O(k) operation, kills speed
                curr = s[l]
                if curr in counts:
                    if counts[curr] == temp[curr]:  # in case removing the current element will now be less than the required count for that character
                        to_match += 1  # increment to_match
                    temp[curr] -= 1  # decrement its count
                l += 1  # move pointer
        if res is not None:
            return s[res[0]:res[1]+1]  # now finally we slice using the best indices
        return ""
