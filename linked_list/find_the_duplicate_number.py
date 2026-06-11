class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # imagine that each number in the list represents the node number / index
        # so if you follow this, at some point, an index will repeat
        # as in 2 nodes are pointing to the same node (a cycle)
        # and the node number is the duplicate number hence
        # FLOYD's CYCLE DETECTION

        slow = nums[0]
        fast = nums[nums[0]]

        # reach where slow and fast meet
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0

        # then start from the start and the collision point together
        # but slow style
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
        
        
