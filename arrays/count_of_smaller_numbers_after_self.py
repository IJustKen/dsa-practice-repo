#Given an integer array nums, return an integer array counts where counts[i] 
#is the number of smaller elements to the right of nums[i]


#Here is the logic. We start iterating from the end of the list
#example - [5,1,2,6] we start from 6. We keep track of a sorted list also on the side and basically see which index 
#we can insert the current elem. So starting the sorted list is [] and we look at 6, obv it inserts at 0.
#So now we have sorted - [6] and now move to next elem from the back which is 2. See where can 2 be inserted? at the 0th index.
#So [2,6]. Notice that the index where I am inserting it is equivalent to the number of elem smaller to the number on the right
#in the OG list.
#When we get to inserting 5 in [1,2,6] it goes at index 2. And that is indeed the num of elem smaller on the right.
#For duplicates we gotta make sure that we choose the left most index of the existing number. like insert 5 in [1,2,5,6] it should go at 
#idx 2 not anywhere else to be consistent with the index logic

#start from back cuz we seeing nums smaller on the right no. This way no inconsistency. Like if I say 6 inserts at idx 0, then 
# nums on the right of 6 are indeed zero. In the future also there are no elems getting added on the right so yeah 



from sortedcontainers import SortedList     #maintain a sorted list (heap type)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = SortedList([])
        ans = []
        for i in range(len(nums)-1,-1,-1):      #start from the back
            num = nums[i]
            idx = sorted_list.bisect_left(num)      #get the leftmost index possible in the sorted list for the num
            ans.append(idx)                         #append idx which is the num of smaller elem on right
            sorted_list.add(num)                    #add num to sorted list
        return ans[::-1]                        #final list is in reverse obv



        