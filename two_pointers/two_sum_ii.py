#Approach 1: O(n) solution we can try since the array is sorted non decreasing order
# True 2 pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) -1
        while p1<p2:
            curr_sum = numbers[p1] + numbers[p2]    # this was the main overhead, do not keep doing n1+n2 in each if statement, just calculate sum once and reuse
            if curr_sum > target:
                p2 -= 1
            elif curr_sum < target:
                p1 += 1
            else:
                return [p1+1, p2+1]


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
