from typing import List


# 题目链接:https://leetcode.cn/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 初始化窗口
        left, right, sm = 0, 0, 0
        # 这里初始值设置为len(nums)+1即可
        # ans = float('inf')
        ans = len(nums) + 1
        while right < len(nums):
            sm += nums[right]
            while sm >= target:
                ans = min(ans, right - left + 1)
                sm -= nums[left]
                left += 1
            right += 1
        return 0 if ans == len(nums) + 1 else ans
