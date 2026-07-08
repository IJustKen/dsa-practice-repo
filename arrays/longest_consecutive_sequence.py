class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = set(nums)  # much faster than doing counts = set() and then looping through nums and doing counts.add(), 
        # cuz this is built in method in C
      
        res = 0  # final ans
        temp = 1  # curr seq length
        for num in iter(counts):  # iterate through counts, not nums because nums might have duplicates of many of the sequence starting numbers
          # which will cause TLE
            if num-1 in counts:  # if the current number is not the start of a sequence, skip it
                continue
            nxt = num+1  
            while nxt in counts:  # keep counting as long as consecutive numbers are found
                temp += 1
                nxt = nxt + 1
            res = max(temp, res)  # update max
            temp = 1  # reset seq length

        return res
