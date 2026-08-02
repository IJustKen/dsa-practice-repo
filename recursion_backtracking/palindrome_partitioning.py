#Given a string s, partition s such that every substring of the partition is a palindrome. 
#Return all possible palindrome partitioning of s.


# SLOW ASF solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPali(text):
            # Each of these will go as O(n) calls that is kinda slow when done repeatedly
            ans = True
            for i in range(len(text)//2):
                ans = ans and (text[i] == text[len(text)-i-1])
            return ans
        
        def dfs(pali: list, temp: list, idx: int):
            nonlocal res
            if idx >= len(s):
                if isPali(pali):
                    # join will also be O(n)
                    temp.append("".join(pali.copy()))
                    res.append(temp.copy())
                    temp.pop()
                return

            if not isPali(pali):
                # O(n) call
                pali.append(s[idx])
                dfs(pali, temp, idx+1)
                pali.pop()
                return

            if pali:
                temp.append("".join(pali.copy()))    #O(n)
                dfs([s[idx]], temp, idx+1)
                temp.pop()

            pali.append(s[idx])
            dfs(pali, temp, idx+1)
        
        dfs([], [], 0)
        return res




  #well so if you look at the recursion tree it is like this
  #start from say string aab - you can make 3 parts a, aa or aab. Now aab is not pali so prune it
  #a and aa are pali so continue. Now for 'a' the remaining letters are ab - so furhther branches 'a' and 'ab' of which ab is
  #not pali so prune. 'a' is pali. Now remaining 'b' only which is also pali. This entire brancg gave us 'a','a','b' see.
  #now recall the 'aa' earlier - remaining only 'b' which is pali so 'aa','b' also allowed.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []      

        def isPali(sub):  
            # helper to check palindrome or not
            return sub == sub[::-1]

        def dfs(i):
            nonlocal res
            nonlocal part
            # base case exit after appending to res
            if i>=len(s):     
                res.append(part.copy())    
                return
              
            for j in range(i+1,len(s)+1): 
                # index starts from i till j, j increases one by one
                sub = s[i:j]    # possible substring that could be palindrome
                if isPali(sub):
                    part.append(sub)      # partition here
                    dfs(j)                    
                    part.pop()    # do not partition here, check next bigger substring now
        
        dfs(0)
        return res

        
