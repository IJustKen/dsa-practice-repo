class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #a weirder approach to prefix sum
        prefix_sum = nums
        for i in range(1, len(nums)):
            prefix_sum[i] += prefix_sum[i-1]
        
        prefix_sums_dict = {}
        prefix_sums_dict[0] = 1     #think of a sum zero right outside the nums list on the left
        
        #genius logic - we keep track of the prefix_sums that we have found so far
        #then we see how much the current prefix sum if far from the target
        #say it is off by +2, then we check how many times before we got a prefix sum of +2
        #that basically is equal to the number of subarrays that include the curr elem that sum up to target 

        #say I reached [1,-1,1,1] the last 1 in this, and target is 2. I shall see difference bw curr prefix sum and target which is 0
        #then I see how many times did i get sum 0 before - once outide array, and once inside (prefix sums - 0[1,0,1,2]) meaning I have 2 subarrays including
        #the last elem (1) namely [1,-1,1,1] and [1,1] that sum up to target
        #the zero outside is basically to say the sum of subarray from the start to curr elem
        
        count = 0 
        for i in range(len(nums)):
            diff = prefix_sum[i] - k
            if diff in prefix_sums_dict:
                count += prefix_sums_dict[diff]

            if prefix_sum[i] in prefix_sums_dict:
                prefix_sums_dict[prefix_sum[i]] += 1
            else:
                prefix_sums_dict[prefix_sum[i]] = 1

        return count