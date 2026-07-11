# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node, count):
        # I ONLY CALL THIS IF K NODES ARE AVAILABLE ELSE NOPE DO NOT CALL THIS
        # returns start, end of the reversed node up to k nodes starting from node
        # also returns the next node in original sequence
        if not node:
            return None, None
        prev = None
        nxt = None
        last = node
        curr = node
        while count>0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count -= 1
        start = prev    # renaming to understand but yeah logically prev and curr are the start of reversed list, and the next element of original list
        nxt = curr    # since we disconnected this sub part from original list, we need the new head of the original list, which is this
        
        return start, last, nxt
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode()    # starting boundary of new list
        res_curr = new_head    # curr tracker for this result list

        curr = head    # curr tracker of OG list
        start = curr    # this is to track the starting node of a k (or less than k) length sub part
        counter = 0    # to track how many elements till now
        
        while curr:
            counter += 1    # increment number of nodes seen till now
            if counter == k:    # if we got k nodes, only now call reverse helper function
                n1, n2, nxt = self.reverse(start, k)    # get the start, end of reversed list, and the new head of original list
                res_curr.next = n1    # link result list to start
                res_curr = n2    # jump result curr pointer to the last node in result list, which is the end of the reversed sub sequence
                curr = nxt    # new head
                start = curr    # this may be the start of a k length sub list now
                counter = 0
            else:
                curr = curr.next    # just move forward
        
        if counter > 0:    # after everything if counter is non zero, it means in the end, we could not find a sub sequence of length k, only less than that
            if start:    # thus if that is the case, just link it directly without reversing
                res_curr.next = start

        return new_head.next    # return boundary.next as new head
