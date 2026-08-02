#Given a string s, partition s such that every substring of the partition is a palindrome. 
#Return all possible palindrome partitioning of s.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPali(text):
            ans = True
            for i in range(len(text)//2):
                ans = ans and (text[i] == text[len(text)-i-1])
            return ans
        
        def dfs(pali: list, temp: list, idx: int):
            nonlocal res
            if idx >= len(s):
                if isPali(pali):
                    temp.append("".join(pali.copy()))
                    res.append(temp.copy())
                    temp.pop()
                return

            if not isPali(pali):
                pali.append(s[idx])
                dfs(pali, temp, idx+1)
                pali.pop()
                return

            if pali:
                temp.append("".join(pali.copy()))
                dfs([s[idx]], temp, idx+1)
                temp.pop()

            pali.append(s[idx])
            dfs(pali, temp, idx+1)
        
        dfs([], [], 0)
        return res


class Solution:

  #well so if you look at the recursion tree it is like this
  #start from say string aab - you can make 3 parts a, aa or aab. Now aab is not pali so prune it
  #a and aa are pali so continue. Now for 'a' the remaining letters are ab - so furhther branches 'a' and 'ab' of which ab is
  #not pali so prune. 'a' is pali. Now remaining 'b' only which is also pali. This entire brancg gave us 'a','a','b' see.
  #now recall the 'aa' earlier - remaining only 'b' which is pali so 'aa','b' also allowed.

  
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []      #to append the palis alog one partitioning style

        def isPali(s,i,j):      #helper function to check if palindrome
            if s[i:j+1] == s[i:j+1][::-1]:
                return True
            return False

        def dfs(i):
            nonlocal res
            nonlocal part
            if i>=len(s):      #i is the idx of the letter we are starting from to check pali
                res.append(part.copy())    #base case when all letters are done, we must've reached the end and obtained a partition
                return
              
            for j in range(i,len(s)):    #else, like explained in sol, we keep trying substrings of increasing lengths
                                          #starting from i going all the way to len(s)
                if isPali(s,i,j):
                    part.append(s[i:j+1])      #append the curr pali
                    dfs(j+1)                    #do dfs and look for this particular partitioning style
                    part.pop()            #remove the pali you just found to look for other way of partitioning (diff pali)
        
        dfs(0)
        return res

        
