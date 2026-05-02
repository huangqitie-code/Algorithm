from typing import List


# 题目链接:https://leetcode.cn/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(board: List[List[str]], row: int, col: int) -> bool:
            for i in range(9):
                # 检查行是否重复
                if board[i][col] == board[row][col] and i != row:
                    return False
                # 检查列是否重复
                if board[row][i] == board[row][col] and i != col:
                    return False
                # 检查所属3*3九宫格是否重复
                if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == board[row][col] and row != (
                        row // 3) * 3 + i // 3 and col != (col // 3) * 3 + i % 3:
                    return False
            return True

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    if not isValid(board, row, col):
                        return False
        return True
