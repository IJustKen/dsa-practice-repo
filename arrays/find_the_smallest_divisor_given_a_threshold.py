#Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, 
#divide all the array by it, and sum the division's result. Find the smallest divisor such that the result 
#mentioned above is less than or equal to threshold.

#Each result of the division is rounded to the nearest integer greater than or equal to that element. 
#(For example: 7/3 = 3 and 10/2 = 5).

#The test cases are generated so that there will be an answer.


import math    #to use ceil function

class Solution:

  #logic - min divisor can be 1, max can be the max value inside the nums list
  #But then going over all of em is redundant. Notice when you find the min divisor for which threshold is reached,
  #all the divisors after it will also satisfy it cuz the sum will reduce as the result of each division is reduced
  #and similarly the divisors before will all not satisfy
  #so it is like finding the left most "satisfies"
  #like an arrangement of FFFFFTTTTTTTTTT and you are finding the leftmost T

  
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def getsum(arr,d):    #helper function to get the sum given a specific divisor
            temp = 0
            for num in arr:
                temp += math.ceil(num/d)
            return temp
    
        max_div = max(nums)
        low = 1            #our pointers
        high = max_div      #points to the v last divisor

        while low<=high:
            mid = (low+high)//2
            if getsum(nums,mid) <= threshold:      #if we land on T we go left to see if there are more T
                high = mid-1
            else:
                low = mid+1          #if we land on F then obv T would be somewhere right so go right
        return low        #after all swapping is done, the low pointer points to the leftmost T (VISUALISE AND SEE)
         


        
