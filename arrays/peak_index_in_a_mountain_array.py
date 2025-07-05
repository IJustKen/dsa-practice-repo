#You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
#Return the index of the peak element.
#Your task is to solve it in O(log(n)) time complexity.


class Solution:
    
    #binary search style but modified stop conditions basically
  
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = (high+low)//2
            if mid-1>=0 and mid+1<=len(arr)-1:
                if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:      #condition for peak/maxima
                    return mid
                elif arr[mid]<arr[mid-1]:    #else conditions to search left or right partitions accordingly
                    high = mid-1
                elif arr[mid]<arr[mid+1]:
                    low = mid+1
            elif mid-1>=0:      #other conditions for consistency of low and high and thus the while loop
                if arr[mid]<arr[mid-1]:
                    high = mid-1
                else:
                    low = mid+1
            elif mid+1<=len(arr)-1:    #same as above
                if arr[mid]<arr[mid+1]:
                    low = mid+1
                else:
                    high = mid-1
                

            



        
