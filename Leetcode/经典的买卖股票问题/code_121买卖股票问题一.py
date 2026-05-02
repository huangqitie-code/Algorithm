from typing import List


# 题目链接:https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思路是在每一天都把股票卖出时 所能获得的最大收益取最大值
        # 而每天卖出股票的最大收益得益于之前天最低价买入
        # 所以需要获取之前天股票的最低价格
        # 但是要注意如果之前的最低价格大于当前价格 那直接选择当日买当日卖，利润为0
        if not prices:
            return 0
        n = len(prices)
        ans = 0
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(prices[i], min_price)
            ans = max(ans, prices[i] - min_price)
        return ans

