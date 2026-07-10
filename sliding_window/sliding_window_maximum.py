# O(n) solution with deque
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == n:
            return [max(nums)]  # base case do not forget to make it a list

        dq = deque()
        res = []  # store final ans  
        for i in range(k):  # the very first window get the max and populate the deque
            j = i
            while dq and dq[-1] < nums[i]:  # basically if we encounter a number greater than what is in the right most side of deque
              # then pop from right until that is not the case, we only want what is maximum in the window to be on the left most of the deque
              # thus if there is a smaller number on the left then pop it before you append the larger number
                dq.pop()
            dq.append(nums[i])
        res.append(dq[0])
        
        for i in range(k,n):  # now for the remaining array
            rem = nums[i-k]  # the element to be removed from the window
            if rem == dq[0]:  # if it happens to be the left most element in the deque (that is, the greatest in the current window)
                dq.popleft()  # then remove it from deque also
        
            while dq and dq[-1] < nums[i]:  # if you get a greater number to be appended
                dq.pop()  # first pop from right until that is not the case, because we want left most value to be the greatest value in current window
            dq.append(nums[i])
            res.append(dq[0])  # left most element is the greatest in the current window, so append to res
        
        return res




# this one is O(nlogn) because each push operation is logn worst case and we are doing it O(n) times.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == n:
            return [max(nums)]
        heap = []
        res = []

        heap_counts = dict()
        window_counts = dict()

        for i in range(k):
            heapq.heappush(heap, -nums[i])
            heap_counts[nums[i]] = 1 + heap_counts.get(nums[i],0)
            window_counts[nums[i]] = 1 + window_counts.get(nums[i],0)
        res.append(-heap[0])

        
        for i in range(k, n):
            heapq.heappush(heap, -nums[i])
            heap_counts[nums[i]] = 1 + heap_counts.get(nums[i],0)
            window_counts[nums[i]] = 1 + window_counts.get(nums[i],0)
            window_counts[nums[i-k]] -= 1
            if -nums[i-k] == heap[0]:
                while heap_counts[-heap[0]] > window_counts[-heap[0]]:
                    popped = -heapq.heappop(heap)
                    heap_counts[popped] -= 1
            res.append(-heap[0])

        return res
