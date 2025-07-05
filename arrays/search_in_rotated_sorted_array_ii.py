#same as search in rotated sorted array but with duplicates


class Solution:

  #same approach as before except there is one problem - the criteria to check whether left partition is sorted or the right
  #so that case is handled 
  
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[l] and nums[mid] == nums[r]:   #here we cant tell which side is sorted so I just decrement r
                r -= 1    
                continue        #keep doing until this condition aint satisfied
            elif nums[mid] == nums[l]:    #if it didnt pass the above, then obv l to mid is the same number so search right
                l = mid+1
            elif nums[mid] == nums[r]:    #same logic, search left
                r = mid-1
            elif nums[mid] >= nums[l]:    #this is the same as earlier but we remove the condition of "or target > nums[r]"
                if (nums[mid] > target and target >= nums[l]):
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid]<= nums[r]:    #similar here
                if (nums[mid]< target and target<=nums[r]):
                    l = mid+1
                else:
                    r = mid-1
        return False
