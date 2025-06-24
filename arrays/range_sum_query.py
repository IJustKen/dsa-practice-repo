#Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

#WE DOING PREFIX SUM CUZ MULTIPLE QUERIES OF SUMMING OVER LIST HAVE BEEN ASKED
#Only one or two queries we could have written the usual way iterating left to right
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = nums
        for i in range(1,len(nums)):
            self.prefix_sum[i] += self.prefix_sum[i-1]      #make this list of the sum of the prefix (all elems before plus the element itself)
        print(self.prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
    
        if left >= 1:
            return self.prefix_sum[right] - self.prefix_sum[left-1]
        if left == 0:
            return self.prefix_sum[right]
        else:
            return 0

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
