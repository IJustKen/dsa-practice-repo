# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # reverse the second half of linked list approach

        # edge 
        if head.next is None:
            return head
        if head is None:
            return None
        
        # find mid point
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # mid is the slow pointer
        # cut it off from the first part, mid will be part of second half
        prev.next = None

        # reversing second half
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        p1 = head
        p2 = prev
        
        #logic based on the example figure out
        while p1.next and p2:
            temp1 = p1.next
            temp2 = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = temp1
            p2 = temp2
        if p1.next is None and p2 is not None:
            p1.next = p2
