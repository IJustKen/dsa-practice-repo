# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

#Detect if cycle is there and return the node where cycle is starting


class Solution:

  #recall the video intuition in this. Basically we do the usual tortoise and hare stuff. Now the node where slow and fast 
  #meet is mathematically at the same distance from target node, as the head is from the target node.
  #draw a figure and see it geometrically if needed.
  

  
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:    #edge case
            return None

        slow = head        #tortoise and hare
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:        #modification here, so this means we found cycle
                slow = head          #no we start from head, and also from the collided node
                                      #since they are both at same distance from cycle starting node, they will def collide
                                    #you can use a new pointer also but why use more memory lol
                                    #iterate until you collide
                while slow != fast:                
                    slow = slow.next
                    fast = fast.next
                return fast                #return either fast or slow both same
                

        return None        #no cycle found
        
