# BINARY SEARCH
# yeah so the concept is that we need to find cuts in both the array such that it represents the boundary between the right and left elements
# by right and left, I mean if both arrays were combined, which ones would go left and which ones right, like that.
# so we need to find that boundary. Now the thing is, at that boundary there will be equal elements on left and right side
# which means that if I choose boundary in the smaller array at index i, then I can automatically pick the first (total/2 - i) elements from the bigger array
# as the remaining left side elements. Now we have to adjust where we make the cut in the smaller array.
# the stopping condition is when largest element in left side is <= smallest in right side
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):  # i want A to be the smaller array
            A,B = B,A
        
        total = len(A) + len(B)
        half = total // 2  # this will help pick remaining left side elements in B

        l, r = 0,len(A)-1  # so we do binary search in A, to find where the cut would be

        while True:  # cuz the median is guaranteed
            mid = math.floor((l+r)/2)  # standard binary search, this is the index of the cut in A
            left1 = mid+1  # num of elements picked in smaller list
            left2 = half - left1
            left_idx = left2-1  # this is the index of the cut in B

            Aleft = A[mid] if mid>=0 else float("-inf")  # element in A, part of the left side
            Aright = A[mid+1] if (mid+1) < len(A) else float("inf")  # element in A, part of the right side
            Bleft = B[left_idx] if left_idx>=0 else float("-inf")  # else conditions are for when out of bounds happens, that is, when your cut full includes or excludes A
            Bright = B[left_idx+1] if (left_idx+1) < len(B) else float("inf")  # in that case also, the stopping condition has to be met, thus accordingly we kept values

            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 0:  # even number of elements, take average of middle 2 elements
                    return (max(Aleft, Bleft) + min(Aright,Bright))/2  # that will be max from left side, and min from right side
                return min(Aright, Bright)  # odd number of elements, pick the smallest element from right side, that will be the middle
            
            elif Aright < Bleft:  # Aright must be made bigger, so move right
                l = mid+1
            elif Aleft > Bright:  # Aleft must be made smaller, so move left
                r = mid-1
