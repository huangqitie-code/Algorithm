from typing import List


# 题目链接:https://leetcode.cn/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        我们可以利用矩阵的第一行和第一列来记录哪些行和列需要被置零。具体步骤如下：

        使用两个标志变量记录第一行和第一列是否包含 0。

        遍历矩阵，用第一行和第一列记录需要置零的行和列。

        根据第一行和第一列的记录，将对应的行和列置零。

        根据标志变量处理第一行和第一列。
        """
        # 这是空间复杂度O(1)的做法
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any([matrix[0][i] == 0 for i in range(n)])
        first_col_has_zero = any([matrix[i][0] == 0 for i in range(m)])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0

        if first_row_has_zero:
            for i in range(n):
                matrix[0][i] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        # 空间复杂度O(m+n)的算法
        m, n = len(matrix), len(matrix[0])
        # 额外列表记录每一行和每一行是否有零元素
        matRow = [False] * n
        matCol = [False] * m
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matRow[j] = True
                    matCol[i] = True
        for i in range(m):
            if matCol[i]:
                for j in range(n):
                    matrix[i][j] = 0

        for i in range(n):
            if matRow[i]:
                for j in range(m):
                    matrix[j][i] = 0


Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
