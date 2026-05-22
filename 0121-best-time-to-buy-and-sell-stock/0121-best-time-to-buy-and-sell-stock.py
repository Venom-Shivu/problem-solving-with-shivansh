class Solution:
    def maxProfit(self, prices):

        min_price = prices[0]

        max_profit = 0

        for price in prices[1:]:

            if price < min_price:

                min_price = price

            else:

                diff = price - min_price

                if diff > max_profit:
                    max_profit = diff

        return max_profit