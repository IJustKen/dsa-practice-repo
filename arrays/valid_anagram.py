#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
  #anagram means basically you can make one word with the other word
  #with the exact same letters
  #so we can just check the chars present in each word and if their frequency matches they are anagrams
    def isAnagram(self, s: str, t: str) -> bool:
      
        s_ch = dict()      #maintain chars and their counts
        t_ch = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in s_ch:
                s_ch[s[i]] += 1
            else:
                s_ch[s[i]] = 1
            if t[i] in t_ch:
                t_ch[t[i]] += 1
            else:
                t_ch[t[i]] = 1
        if s_ch == t_ch:      #finally if every key value pair matches then we chill
            return True
        return False

        
