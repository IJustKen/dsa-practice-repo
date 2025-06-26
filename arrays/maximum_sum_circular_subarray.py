class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        #logic is you get the subarray with the minimum sum and subtract it from the total sum
        #also keep track of maxsum and minsum within the array
        #see if the maxsum is on the edge of the list then minsum array cant be on the edge as well obv
        #so minsum must be in the normal array so in the end subtract it from the total
        #if maxsum is within the normal array then minsum will be on the edge (may or may not cross it)
        #in that case you maxsum will be the direct maxsum you find

        total, maxSum, curMax, minSum, curMin = 0,nums[0],0,nums[0],0
        for num in nums:
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
            total += num
        if maxSum > 0:
            return max(maxSum, total - minSum)
        else:
            return maxSum

