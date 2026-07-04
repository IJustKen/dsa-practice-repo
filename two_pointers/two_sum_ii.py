#Approach 1: O(n) solution we can try since the array is sorted non decreasing order




# Approach 2: slow as this is O(nlogn)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        res = []
        for i in range(n):
            l = i+1
            h = n-1
            find = target - numbers[i]
            while l<=h:
                mid = (l+h)//2
                if numbers[mid] == find:
                    res.append(i+1)
                    res.append(mid+1)
                    return res
                elif numbers[mid] > find:
                    h = mid-1
                elif numbers[mid] < find:
                    l = mid+1
