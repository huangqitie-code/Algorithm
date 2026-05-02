from typing import List


# 题目链接:https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/?envType=study-plan-v2&envId=top-interview-150
# 如果不懂去看左神B站视频:https://www.bilibili.com/video/BV1PN411j7aG/?vd_source=81d53d51554db93d253a255693fa8624
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def free(prices: List[int]) -> int:
            ans = 0
            for i in range(1, len(prices)):
                ans += max(0, prices[i] - prices[i - 1])
            return ans

        n = len(prices)
        if k > n // 2:
            return free(prices)

        # dp[k][n]代表在0...n范围上做不超过k次交易所能获得的最大利润
        # 状态转移讨论分为在第n天不做交易和做交易
        # 在第n天不交易则dp[k][n]=dp[k][n-1]
        # 在第n天做交易必然是卖出股票 则需要往前找寻找买入时机
        # 买入时机是i的话，则dp[k][n]=dp[k-1][i]+prices[n]-prices[i] 0<=i<=n
        # 通过观察枚举发现 dp[k][n+1]=dp[k-1][i]+prices[n+1]-prices[i] 0<=i<=n+1
        # 得到两个dp的相同枚举部分为dp[k-1][i]-prices[i]部分
        # 所以在遍历的时候用一个best变量来更新枚举部分的最好值 替换掉枚举部分

        dp = [[0] * n for _ in range(k + 1)]
        # 提交力扣目前是超时的 Java不超时 python超时
        # for i in range(1, k + 1):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i][j-1]
        #         for m in range(j + 1):
        #             dp[i][j] = max(dp[i][j], dp[i-1][m] + prices[j] - prices[m])
        # 使用best优化
        for i in range(1, k + 1):
            best = dp[i - 1][0] - prices[0]
            for j in range(1, n):
                best = max(best, dp[i - 1][j] - prices[j])
                dp[i][j] = max(dp[i][j - 1], best + prices[j])
        return dp[k][n - 1]
        # 状态压缩dp二维变一维
        # dp = [0] * n
        # for i in range(1, k + 1):
        #     best = dp[0] - prices[0]
        #     for j in range(1, n):
        #         # 这里的dp[j]实则就是二维下dp[i-1][j]的值 因为dp[j]还没更新
        #         best = max(best, dp[j] - prices[j])
        #         dp[j] = max(dp[j - 1], best + prices[j])
        #
        # return dp[n - 1]


so = Solution()
print(so.maxProfit(2, [3, 2, 6, 5, 0, 3]))
print(so.maxProfit(2, [2, 4, 1]))
