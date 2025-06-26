class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        #easy two pointer logic if curr sum is greater than target obv we have to go lower on the right 
        #if curr sum is lesser then we obv go greater by going higher on the left
        
        while numbers[right] + numbers[left] != target and left < right:
            if numbers[right] + numbers[left] > target:
                right -= 1
            else:
                left += 1
        
        return [left+1,right+1]
        