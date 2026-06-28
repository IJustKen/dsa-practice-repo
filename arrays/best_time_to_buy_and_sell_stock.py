# KEY: Seems tricky at first but you just have to keep track of the minimum seen so far while iterating through the array.
# Because today, the max profit is basically today minus previously seen lowest price.
# So the best_profits array stores the best possible profit that can be made today.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float('inf')
        best_profits = []

        for val in prices:
            if val<=curr_min:
                curr_min = val  #update the curr min seen so far
                best_profits.append(0)
                continue
            best_profits.append(val-curr_min)  #max profit today is today's price minus last seen lowest price
        return max(best_profits)
        
