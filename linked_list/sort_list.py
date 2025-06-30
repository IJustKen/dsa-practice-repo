#Given the head of a linked list, return the list after sorting it in ascending order.




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    #So we shall do mergesort for linked list, fastest. First thing find the middle element ofc, for that v common method is
    #slow n fast pointers. Once you get middle elem, split the linked list by making the middle.next = None
    #then it is recursive
    #helper merge function is also used, same logic as merging in normal list

    def merge(self, a1,a2):
        dummy = ListNode(0)     #dummy node to initially start linking from
        curr = dummy
        while a1 and a2:
            if a1.val < a2.val:
                curr.next = a1
                a1 = a1.next
            else:
                curr.next = a2
                a2 = a2.next
            curr = curr.next
        if a1:
            curr.next = a1
        if a2:
            curr.next = a2
        return dummy.next       #return dummy.next cuz that is where the merged linked list lies

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:           #base case
            return head
        slow, fast = head,head      #slow and fast pointers for detecting middle
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left,right)

        

        

        