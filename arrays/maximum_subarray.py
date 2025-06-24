class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum = nums[0]       #initialise the max sum as the first num
        cursum = 0          #initialise curr sum

        for num in nums:        #iterate through list, and keep track of cumulative sum, if it becomes negative it means we can ignore
            if cursum < 0:      #the entire portion on its left because it will only reduce the sum so we ignore 
                cursum = 0          #thus we reset the cursum to 0 basically starting the subarray next element onwards
            cursum += num
            maxsum = max(cursum, maxsum)        
        return maxsum



            


        