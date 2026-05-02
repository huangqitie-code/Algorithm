from typing import List


# 题目链接:https://leetcode.cn/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 使用动态规划 python超时了 Java不会
        # if len(nums) < 2:
        #     return True
        # dp = [False] * len(nums)
        # dp[0] = True
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if dp[j] and nums[j] >= i - j:
        #             dp[i] = True
        #             break
        # return dp[len(nums) - 1]
        # 使用贪心算法
        # 设想一下，对于数组中的任意一个位置y，我们如何判断它是否可以到达？根据题目的描述，只要存在一个位置x，它本身可以到达，并且它跳跃的最大长度为
        # x + nums[x]，这个值大于等于y，即x + nums[x]≥y，那么位置y也可以到达。
        # 换句话说，对于每一个可以到达的位置x，它使得x + 1, x + 2,⋯, x + nums[x]
        # 这些连续的位置都可以到达。
        # 这样以来，我们依次遍历数组中的每一个位置，并实时维护
        # 最远可以到达的位置。对于当前遍历到的位置x，如果它在
        # 最远可以到达的位置的范围内，那么我们就可以从起点通过若干次跳跃到达该位置，因此我们可以用x + nums[x]更新
        # 最远可以到达的位置。
        # 在遍历的过程中，如果最远可以到达的位置 大于等于数组中的最后一个位置，那就说明最后一个位置可达，我们就可以直接返回True
        # 作为答案。反之，如果在遍历结束后，最后一个位置仍然不可达，我们就返回False作为答案。
        maxPosition,n = 0, len(nums)
        for i in range(n):
            if i <= maxPosition:
                maxPosition = max(maxPosition, i + nums[i])
                if maxPosition >= n - 1:
                    return True
        return False
