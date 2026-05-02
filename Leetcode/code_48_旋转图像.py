from typing import List


# 题目链接:https://leetcode.cn/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 首先分析下坐标转换 得到一般规律
        # 以3*3为例
        # (0,0)->(0,2)
        # (0,1)->(1,2)
        # (0,2)->(2,2)
        # (1,0)->(0,1)
        # (1,1)->(1,1)
        # (1,2)->(2,1)
        # 这里可以看出(i,j)变换后的坐标是(j,n-i)可以看成是(i,j)->(j,i)->(j,n-i)
        # 所以思路是先转置 后交换首尾列
        n = len(matrix)
        for i in range(n):
            for j in range(0,i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(n):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = temp
        print(matrix)

Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])
