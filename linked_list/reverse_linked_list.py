# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#reverse a singly linked list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None      #to keep track of prev node
        while curr:
            temp = curr.next    #save the next node
            curr.next = prev      #point next to prev (reversing no)
            prev = curr      #new prev
            curr = temp      #the saved node is new curr
        
        return prev
        
