from typing import List


# 题目链接:https://leetcode.cn/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 说不上难 考验逻辑
        ans = []
        if not matrix or not matrix[0] or len(matrix[0]) == 0:
            return ans
        row_start, row_end, col_start, col_end = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while row_start <= row_end and col_start <= col_end:
            for col in range(col_start, col_end + 1):
                ans.append(matrix[row_start][col])
            row_start += 1
            if row_start <= row_end:
                for row in range(row_start, row_end + 1):
                    ans.append(matrix[row][col_end])
                col_end -= 1
            if row_start <= row_end and col_start <= col_end:
                for col in range(col_end, col_start - 1, -1):
                    ans.append(matrix[row_end][col])
                row_end -= 1
            if row_start <= row_end and col_start <= col_end:
                for row in range(row_end, row_start - 1, -1):
                    ans.append(matrix[row][col_start])
                col_start += 1
        return ans
