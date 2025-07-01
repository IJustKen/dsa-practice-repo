#Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

import random
class Solution:

    #fastest way to first sort and then get index len(nums)-k
    #Here is another way of using quickselect
    #Logic is kinda like quicksort where we select a pivot and then put nums less than and greater than on left and right of it.
    #Then depending on k we further look in the right partition or left partition.
    #We are using 2 pointer l and r to decide from where to where in the nums we are looking


    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        def quickselect(l,r):
            pivot_idx = random.randint(l,r)
            pivot, pointer = nums[pivot_idx], l
            nums[pivot_idx],nums[r] = nums[r],nums[pivot_idx]       #swap pivot with last elem
            for i in range(l,r):                #in the permitted range, do the swapping thing as in quicksort
                if nums[i] <= pivot:
                    nums[i],nums[pointer] = nums[pointer],nums[i]
                    pointer += 1                #this pointer tells where to swap next time

            nums[r],nums[pointer] = nums[pointer],nums[r]       #finally swap the pivot back from the end

            if pointer < k:             #kth largest must be on the right partition
                return quickselect(pointer+1,r)     
            elif pointer > k:           #kth largest must be on the left partition
                return quickselect(l,pointer-1)
            else:
                return nums[pointer]    #pivot is the kth largest
            

        return quickselect(0,len(nums)-1)       #start with full array

        