#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

class Solution:

  #similar to the other sliding window question we did where we see how many times
  #a certain substring comes in a given string
  #same logic we use a hashmap of the count of chars in s and p and iterate accordingly
  
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p)>len(s):      #anagram impossible if p is bigger than s
            return res      
        t_ch = DefaultDict(int)    #to see required counts to be anagram with p
        for i in range(len(p)):
            t_ch[p[i]] += 1
          
        p1 = 0
        p2 = len(p)-1
        s_ch = DefaultDict(int)
        for i in range(len(p)):      #input the first len(p) chars into the hashmap of s
            s_ch[s[i]] += 1
          
        while p2 <= len(s)-1:
            if t_ch == s_ch:    #if char counts match then return the starting index
                res.append(p1)
            s_ch[s[p1]] -= 1    #then remove the p1 wala elem and add the p2+1 wala
                                #this is sliding window
            if s_ch[s[p1]] == 0:
                del s_ch[s[p1]]      #this i did because elem whose count 0 were still present
                                    #messing up the t_ch == s_ch thing
            if p2+1 <= len(s)-1:    #for consistency we check p2+1 else it will become out of bounds
                s_ch[s[p2+1]] += 1      #adding next char into the window
            p1 += 1                      #increment both pointers
            p2 += 1
        return res

        
            
        
        
