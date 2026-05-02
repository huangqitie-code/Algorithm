from typing import List


# 题目链接:https://leetcode.cn/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 动态规划超时版本
        # n = len(nums)
        # dp = [n] * n
        # dp[0] = 0
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] >= i - j:
        #             dp[i] = min(dp[i], dp[j] + 1)
        #             break
        # return dp[n - 1]
        # 贪心
        # step表示发生多少步数
        # cur_max_distance表示发生step步能到达的最远位置
        # next_max_distance表示发生step+1步能到达的最远位置
        step, cur_max_distance, next_max_distance = 0, 0, nums[0]
        for i in range(1, len(nums)):
            # 超过当前步数最远位置 则步数+1 cur_max_distance更新为next_max_distance
            # 每次遍历都去更新next_max_distance的值
            if i > cur_max_distance:
                step += 1
                cur_max_distance = next_max_distance
            next_max_distance = max(next_max_distance, i + nums[i])
            # 这里还可以进行剪枝
            if cur_max_distance >= len(nums) - 1:
                return step
        return 0

