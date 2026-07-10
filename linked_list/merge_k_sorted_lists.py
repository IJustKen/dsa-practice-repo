# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# so brute force would be to keep iterating through the k heads and see which is the smallest, then connect it to the new list
# and do head = head.next for that particular list, and so on.
# but this can go O(k^2.n) because if on average we have n elements in each list, that means we have total kn elements. This method will go through
# all of those and will do it O(k) times, so overall it is O(nk^2)

# but if we use a heap, we can track the smallest head. And at any point, the heap has at max k values only
# so to populate the heap once O(klogk).
# after that, now we keep popping and pushing only, which will be O(kn.logkn) time which is better than O(kn.k) where n is a constant.
# how? there are O(kn) elements, and for each push it takes O(logkn) time worst case.
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = ListNode()
        curr = new_head  # starting boundary of final sorted list
        heap = []    # heap

        for i in range(len(lists)):  # create initial heap
            head = lists[i]  # head of current list
            if head:
              # NOTE: i is v important because min heap for a tuple checks first element; if it's equal, checks second element, so
              # if you keep it as (head.val, head) it will throw error. So keep i as the tie breaker
                heapq.heappush(heap, (head.val, i, head))  # push to min heap if head exists
        
        while len(heap)>0:  # now we iterate until heap is empty
            (val, idx, node) = heapq.heappop(heap)  # pop the minimum element (idx'th list's head)
            curr.next = node  # link to the final result list
            curr = curr.next  # update final result list curr node
            if node.next:  # now we check if the node we popped from the heap, has a next or not, 
              # because we need to get the next node from this particular list now, and then repeat
                node = node.next
                heapq.heappush(heap, (node.val, idx, node))  # push it

        return new_head.next  # new_head was a placeholder, actual starts from next


                


