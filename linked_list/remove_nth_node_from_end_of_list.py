# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        steps = 0
        last = head
        while last.next:
            last = last.next
            steps += 1
        steps += 1

        prev = None
        curr = head
        steps = steps - n
        count = 0
        while count != steps:
            prev = curr
            curr = curr.next
            count += 1

        # delete curr
        if prev is None:
            return curr.next
            
        prev.next = curr.next
        curr.next = None
        return head
