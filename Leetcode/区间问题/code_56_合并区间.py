from typing import List


# 题目链接:https://leetcode.cn/problems/merge-intervals/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 对区间列表进行排序：先按第一个元素升序，如果第一个元素相同则按第二个元素升序
        # intervals.sort(key=lambda x: (x[0], x[1]))
        # 本问题只需要第一个元素升序就行
        intervals.sort(key=lambda x: x[0])
        ans = []
        for interval in intervals:
            # ans为空 或者最后一个元素的右端点小于当前区间的左端点
            # 则直接将当前区间加入ans 因为已经是不重叠区间了
            # 否则就是重叠区间 选择最大的右端点进行更新(因为要囊括肯定选右端点大的)
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
