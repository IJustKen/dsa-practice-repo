# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#k is a positive integer and is less than or equal to the length of the linked list. 
#If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#You may not alter the values in the list's nodes, only nodes themselves may be changed.


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
      
        def revpossible(n):      #helper 
            #to check if remaining linked list has at least k elements or not
            #if not then we dont have to reverse this part hence we need to know          
            i = 0
            while n:
                n = n.next
                i += 1
            if k <= i:
                return True
            else:
                return False
              
        if revpossible(head):          #i reverse the first group
            prev_k_first = head        #first elem of the previous k size group after revsersing
            prev = None
            curr = head
            for i in range(k):            #only up to k elements
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            new_head = prev
        else:
            return head
          
        #what happens is this is now disconnected from the rest, so we gotta logically connect it
        while revpossible(curr):
            prev = None                  #to treat each k size group separately
            for i in range(k):
                if i == 0:
                    first = curr
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            prev_k_first.next = prev        #this step connects the previous reversed group to current
            prev_k_first = first            #update prev_k_first with first of the curr group

        if curr:
            prev_k_first.next = curr      #if any remaining nodes (less than k) then just connect as is
        return new_head                  #the new head is actually the last node of the very first group
        

            
        
        
        

        
