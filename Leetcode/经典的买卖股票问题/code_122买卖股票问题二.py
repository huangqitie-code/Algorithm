from typing import List


# 题目链接:https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思路在于找到所有的股价上升的时刻 在前一刻买入 后一刻卖出
        # 代码处理起来特别方便 每次将prices[i]-prices[i-1]累加
        # 如果相减为负数则不进行相加 去掉这一次
        if not prices:
            return 0
        n = len(prices)
        ans = 0
        for i in range(1, n):
            ans += max(0, prices[i] - prices[i - 1])
        return ans
