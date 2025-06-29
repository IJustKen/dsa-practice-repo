#Given an array of integers nums, sort the array in ascending order and return it.

#You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and 
#with the smallest space complexity possible.


class Solution:

    #this is just mergesort. DO NOT USE list.pop(0), it is actually O(n) because even though we are indexing the removal
    #after that shiftin the list by 1 elem takes O(n) time. Hence see merge function accordingly.

    def merge(self, arr1, arr2):
        res = []
        i,j = 0,0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        res.extend(arr1[i:])
        res.extend(arr2[j:])
        return res
    
    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr   
        #left = self.mergesort(arr[:len(arr)//2])
        #right = self.mergesort(arr[len(arr)//2:])
        return self.merge(self.mergesort(arr[:len(arr)//2]), self.mergesort(arr[len(arr)//2:]))
        

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)



        