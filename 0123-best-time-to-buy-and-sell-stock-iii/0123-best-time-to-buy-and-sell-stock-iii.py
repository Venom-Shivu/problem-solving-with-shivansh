class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for price in prices[1:]:
            if -price > buy1:
                buy1 = -price

            temp = buy1 + price
            if temp > sell1:
                sell1 = temp

            temp = sell1 - price
            if temp > buy2:
                buy2 = temp

            temp = buy2 + price
            if temp > sell2:
                sell2 = temp

        return sell2