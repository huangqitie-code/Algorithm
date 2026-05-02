from typing import List


# 题目链接:https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        ans = []
        mapping = {}
        for i in range(n):
            if target - nums[i] in mapping:
                return [mapping[target - nums[i]], i]
            mapping[nums[i]] = i
        return ans
