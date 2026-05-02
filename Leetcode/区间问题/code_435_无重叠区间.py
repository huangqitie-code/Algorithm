from typing import List


# 题目链接:https://leetcode.cn/problems/non-overlapping-intervals/description/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        使用贪心算法:优先按照右端点从小到大进行排序 因为要想互不重叠区间越多 那么肯定要求首个区间
        右端点越小 可以理解成我怎么安排可以开更多的会议 那肯定是越早结束越好 能留出更多的时间参与其他会议
        """
        intervals.sort(key=lambda x: x[1])
        ans = 1
        n = len(intervals)
        right = intervals[0][1]
        for i in range(1, n):
            if right <= intervals[i][0]:
                ans += 1
                right = intervals[i][1]
        return n - ans
