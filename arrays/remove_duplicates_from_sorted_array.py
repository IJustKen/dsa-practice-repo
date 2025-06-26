class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #beats 100% did myself
        #logic - make one pass over nums and note down where all a new num is seen
        #use a hashmap to map it to the index it belongs to, e.g. - [1,1,2,2,3] here uk first unique elem goes to idx 0, next goes to idx 1
        #and so on, so we map these increasing idxs 0,1,2.. to where in nums we find unique nums, so here {0:0, 1:2, 2:4}
        #then we basically swap nums in these idxs that way we have [1,2,3,_,_]
        #works cuz we only care about the first k unique nums, rest can be anything
        
        pos_num = 0
        swap_idxs = {}
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])
                swap_idxs[pos_num] = i
                pos_num += 1

        for pos in swap_idxs:
            nums[pos],nums[swap_idxs[pos]] = nums[swap_idxs[pos]],nums[pos]
        return len(swap_idxs)
                    