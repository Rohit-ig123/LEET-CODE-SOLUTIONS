class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        index_buy=0
        
        profit=0
        diff=0

        if (len(prices)!=1):
            for j in range(1,len(prices),1):
                if (prices[index_buy]<prices[j]):
                    diff=prices[j]-prices[index_buy]
                    if (diff>profit):
                        profit=diff
                else:
                    index_buy=j
        else:
            return profit
        return profit
        
        
                