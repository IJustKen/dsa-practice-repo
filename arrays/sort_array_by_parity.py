#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

#Return any array that satisfies this condition.

class Solution:

    #simple logic of swapping. First we see where the first even element idx is. Then swap it with the first elem. Now we iterate
    #through the nums from idx 1 to len(num)-1. If we encounter odd num we swap with last known even idx + 1 and increment last known
    #even idx. That is it.

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last_even = None
        for i in range(len(nums)):
            if nums[i]%2 == 0:        #find first even elem idx
                last_even = i
                break
        if last_even == None:
            return nums
        
        nums[last_even],nums[0] = nums[0],nums[last_even]        #swap and make it the first elem
        last_even = 0        #dont forget to update the last_even idx
        for i in range(1,len(nums)):
            if last_even == len(nums)-1:
                break
            if nums[i]%2 == 0:
                nums[i],nums[last_even+1] = nums[last_even+1],nums[i]
                last_even += 1
        return nums
