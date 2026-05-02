from typing import List


# 题目链接:https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        i, j = 0, n - 1
        while i < j:
            if height[i] < height[j]:
                ans = max(ans, (j - i) * height[i])
                i += 1
            else:
                ans = max(ans, (j - i) * height[j])
                j -= 1
        return ans
