
from typing import List

# 题目链接:https://leetcode.cn/problems/coin-change/description/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for num in coins:
                if i >= num:
                    dp[i] = min(dp[i], dp[i - num] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 2
        index = 1  # 表示有效数组的末位那个位置
        for i in range(2, len(nums)):
            if nums[index - 1] != nums[i]:
                nums[index + 1] = nums[i]
                index += 1

        return index + 1


so = Solution()
print(so.coinChange([1, 2, 5], 11))
print(so.coinChange([2], 3))
print(so.coinChange([1], 0))
