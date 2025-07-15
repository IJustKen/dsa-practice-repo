# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Remove the nth node from the end of the list

class Solution:

  #my idea is to convert it to nth node from start
  
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      
        def chainlen(node):    #helper to get length of the linked list
            i = 0
            curr = node
            while curr:
                curr = curr.next
                i += 1
            return i
        
        length = chainlen(head)      #get it
      
        if length == 1:
            return None        #edge case when only one node is there and you remove it
          
        from_start = length - n + 1      #conversion to pos from start of linked list
        curr = head
        for i in range(0,max(0,from_start-2)):    #get to the node right before the node to be removed
            curr = curr.next

        #now curr is the node right before the node to be removed
          
        if curr.next:          #just making sure it exists and only then we do this 
            temp = curr.next      
            curr.next = curr.next.next      #make it point next to next now
          
        if from_start == 1:    #edge case when removed elem is the first node in list
            return temp
        return head      #normal case


        
