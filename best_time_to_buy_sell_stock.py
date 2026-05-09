class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Start with a very large number
        max_profit = 0

        for price in prices:
            # Update min_price if current price is lower
            if price < min_price:
                min_price = price
            # Calculate profit if sold today
            profit = price - min_price
            # Update max_profit if this profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit
            
