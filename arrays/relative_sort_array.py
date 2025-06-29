#Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

#Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
#Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        #Logic - see how many times num of arr2 comes in arr1 and keep count
        #then iterate through arr2 and append the curr number according to the count of it in arr1
        #sort the remaining non arr2 elem separately and append to the other list

        count = defaultdict(int)    #dictionary st keys not existing in it are defaulted to value 0
        arr2_set = set(arr2)        #easy lookup ke liye
        ending = []     #get the nums not in arr2
        final = []
        for num in arr1:
            if num not in arr2_set:
                ending.append(num)
            count[num] += 1
        ending.sort()

        for num in arr2:
            for i in range(count[num]):
                final.append(num)
        
        final.extend(ending)


        return final

 
        
