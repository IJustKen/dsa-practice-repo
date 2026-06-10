# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# DO NOT USE THIS, IT CLASHES WITH INTERNAL CLASS ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        head = None
        prev = None
        itr = 1

        while curr1 or curr2 or carry != 0:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            digsum = v1+v2+carry
            curr = ListNode(digsum%10, None)
            if prev:
                prev.next = curr
            prev = curr
            carry = digsum//10
            if itr == 1:
                head = curr
                itr += 1
            curr1 = curr1.next if curr1 else curr1
            curr2 = curr2.next if curr2 else curr2
        
        return head


        


        
