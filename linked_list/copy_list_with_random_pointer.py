#A linked list of length n is given such that each node contains an additional random pointer, which could 
#point to any node in the list, or null.

#Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
#where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of 
#the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list 
#represent the same list state. None of the pointers in the new list should point to nodes in the original list.

#For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
#Return the head of the copied linked list.

#Node definition
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      
        if not head:                   #edge case
            return None
          
        #my plan - first get a deep copy of just the nodes and the next pointers
        #and during this we also map the original node to its copy with a hashmap
      
        curr = head.next            #we shall start iterating from second node
        start = Node(head.val)      #copyy
        prev = start              #this is the copy
        idxs_copy = dict()      #to map the og node to its copy
        idxs_copy[head] = start
      
        while curr:
            new_node = Node(curr.val)      #make a new node w same value
            prev.next = new_node          #connect the copy's prev node to this new one

            idxs_copy[curr] = new_node     #map original to the copy
  
            curr = curr.next
            prev = prev.next

        #now that we have a map of og and its copies we can set the random pointers too
        #for random we are not making new node, just need to link it properly. New nodes are already made in prev step
        
        curr = head
        copy_curr = start
      
        while curr:
            if curr.random:
                copy_curr.random = idxs_copy[curr.random]       
                #random pointer of the copy list points to the copy of the node that the og node's random points to
              
            curr = curr.next
            copy_curr = copy_curr.next

        
        return start        #head of the copied list we return 

#Beat 94% no help
        


        
