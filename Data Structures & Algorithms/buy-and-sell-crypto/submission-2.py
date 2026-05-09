class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy  = float('inf')
        sell = 0
        profit = 0
        for i in prices:
            if buy > i:
                print(f'${buy} buying and ${sell} at')
                profit = max(profit,sell-buy)
                buy = i
                sell = i
            else:
                if i > sell:
                    sell =i
        return max(profit,sell-buy)
