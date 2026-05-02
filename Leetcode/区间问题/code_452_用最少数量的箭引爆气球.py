from typing import List


# 题目链接:https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        排序气球：首先将气球按照结束坐标（xend）进行升序排序。这样可以帮助我们优先处理结束较早的气球，确保每支箭能尽可能多地射爆后续的气球。
        初始化箭的数量和位置：从第一个气球开始，将第一支箭放在其结束坐标上，并初始化箭的数量为1。
        遍历气球：对于每个后续气球，如果其开始坐标大于当前箭的位置，说明当前箭无法射爆这个气球，需要增加一支新箭，并将其放在当前气球的结束坐标上。否则，当前箭可以射爆这个气球，继续检查下一个气球。
        """
        points.sort(key=lambda x: x[1])
        ans = 1
        current_position = points[0][1]
        for i in range(1, len(points)):
            if current_position < points[i][0]:
                ans += 1
                current_position = points[i][1]
        return ans


print(Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
