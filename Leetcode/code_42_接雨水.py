from typing import List


# 题目链接:https://leetcode.cn/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def trap(self, height: List[int]) -> int:
        # 数学方法 面积相减 时间复杂度O(n) 空间复杂度O(1)
        n = len(height)
        # leftMax, rightMax = 0, 0
        # # leftArea以当前遍历到的最长的高leftMax为长，宽为1的矩形面积叠加之和
        # # rightArea以当前遍历到的最长的高rightMax为长，宽为1的矩形面积叠加之和
        # # heightArea柱子的面积等于height元素之和
        # leftArea, rightArea, heightArea = 0, 0, 0
        # for i in range(n):
        #     if height[i] > leftMax:
        #         leftMax = height[i]
        #     if height[n - 1 - i] > rightMax:
        #         rightMax = height[n - 1 - i]
        #     leftArea += leftMax
        #     rightArea += rightMax
        #     heightArea += height[i]
        # # 整个矩形面积为leftMax*n
        # return leftArea + rightArea - heightArea - leftMax * n
        # 动态规划 时间复杂度O(n) 空间复杂度O(n)
        ans = 0
        # 记录当前柱子左边的最大值
        leftMax = [0] * n
        # 记录当前柱子右边的最大值
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], height[n - i])
        for i in range(1, n - 1):
            if min(leftMax[i], rightMax[i]) > height[i]:
                ans += min(leftMax[i], rightMax[i]) - height[i]
        return ans
