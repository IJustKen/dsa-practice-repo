#Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such
#that every character in t (including duplicates) is included in the window. If there is no such substring,
#return the empty string "".

#The testcases will be generated such that the answer is unique.

class Solution:

  #Use a sliding window but more importantly a hashmap to keep track of counts of chars
  #Here you are not looking for counts to match but to be greater than or equal to what they are
  #in the target string t
  
    def minWindow(self, s: str, t: str) -> str:
        count_t, window = {},{}
        for i in t:        #first get map of chars and counts in t
            if i not in count_t:
                count_t[i] = 1
            else:
                count_t[i] += 1      #can just use DefaultDict(int) to avoid clutter
              
        have, need = 0, len(count_t)    #have indicates the conditions satisfied currently
                                        #need indicates conditions needed to be satisfied
        
        minlen = len(s)+1      #default case to return if no substring found ke liye
        sol = ""
      
        l = 0          #pointer 1
        for right in range(len(s)):      #pointer 2 is iterating, so slider is actually l
            if s[right] in count_t:
                if s[right] in window:
                    window[s[right]] += 1
                else:
                    window[s[right]] = 1      #fancy way to increment count just use DefaultDict(int)
                  
                if window[s[right]] == count_t[s[right]]:     #if for a certain char the count becomes equal
                                                              #means we "have" another condition met
                    have += 1
            
            while have == need:    #step to reduce size of window as long as have == need
              
                if right-l < minlen:
                    sol = s[l:right+1]
                minlen = min(minlen, right-l)
                if s[l] in count_t:        #decrement count of the char we are removing in the window
                    window[s[l]] -= 1      #no need to do if that char is not in count_t hence we did if s[l] in count_t
                  
                    if window[s[l]] < count_t[s[l]]:        #after removal if this isnt satisfied decrement have
                        have -= 1
                l += 1                          #obv increment l that is what we are tryna do
                
                
        return sol


        
