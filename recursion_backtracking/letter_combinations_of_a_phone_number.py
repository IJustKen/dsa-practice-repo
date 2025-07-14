#Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
#that the number could represent. Return the answer in any order.

#A mapping of digits to letters (just like on the telephone buttons)


class Solution:

  #good ques ig, so simple logic of backtracking ok

  
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {2:'abc', 3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}    #map of digit to the possible letters
        res = []        #final result
        meaning = []    #this is to store decoded meanings of the digit string
      
        def dfs(i,j):        #i is to track the idx in digits string, j to track the idx in string associated with that digit
                            #in the nums_dict
          
            if i >= len(digits):    #base case prune here
                if len(meaning) == len(digits):    #append only if this condition
                    res.append(''.join(meaning.copy()))
                return

            if len(meaning) == len(digits):    #base case we have reached a possible meaning
                res.append(''.join(meaning.copy()))
                return
              
            if j >= len(num_dict[int(digits[i])]):    #all possible letters associated with a digit have been exhausted case
                dfs(i+1,0)                          #hence you move to the next idx in digits string (nuext digit basically)
                                                    #and obv start from the 0th index of associated string 
          
            else:                                  #normal case 
                meaning.append(num_dict[int(digits[i])][j])        #try appending a letter
                dfs(i+1,0)                            #case when letter added, so obv we go next digit decode now
                meaning.pop()                  #backtrack
                dfs(i,j+1)                          #case when we chose the next letter for the same digit
        
        dfs(0,0)
        if res == [""]:          #edge case accomodation
            return []
        return res

        
