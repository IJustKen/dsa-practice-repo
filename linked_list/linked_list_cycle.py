#detect cycle in linked list singly connected ofc

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:    #edge case
            return False
        slow = head      #initialise starting pointers slow and fast
        fast = head.next
        while slow and fast and fast.next:
            slow = slow.next          #slow goes one step fast goes two
            fast = fast.next.next
            if slow == fast:          #if they become the same node means cycle
                return True
        return False            #loop exits means either of them reached the end (None) thus no cycle
        
        
