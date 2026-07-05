# IDEA: iterate through array, keep a pivot, then from there you have to find 2 numbers which sum to (-pivot).
# or essentially all three sum to 0. And if we sort the array initially then the 2 sum sub problem can be done in O(n) time
# and then going through pivots is also O(n), the entire thing will become O(n^2) then.
# so essentially by sorting we make sure, the pivot does not repeat, if we land on same pivot as prev one, we skip it.

# We are ultimately finding triplets like: a (first num) + b (second num) + c (third num) = 0
# in order (because we sorted the array)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort() # O(nlogn)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:  # skip until pivot does not repeat
                continue
            l, r = i+1, n-1  # 2 pointer logic for the array to the right of the pivot
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]  # sum of the three numbers
                if curr_sum > 0:  # sum too big reduce it, move right pointer back
                    r -= 1
                elif curr_sum < 0:  # sum too small, move left pointer forward
                    l += 1
                elif curr_sum == 0:  # found a match
                    res.append([nums[i], nums[l], nums[r]])  # save it
                    l += 1  # move left pointer forward
                    while l<r and nums[l] == nums[l-1]:  # move it forward until we see a new second number (b)
                        l += 1
                    # Alternatively we could have also moved right pointer backward until we find a new third number (c)
        return res



        
