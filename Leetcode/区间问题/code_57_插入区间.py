from typing import List


# 题目链接:https://leetcode.cn/problems/insert-interval/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n = len(intervals)
        i = 0
        ans = []
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans
