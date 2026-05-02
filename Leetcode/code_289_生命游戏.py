from typing import List


# 题目链接:https://leetcode.cn/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        在第一次遍历网格时，计算每个细胞的活邻居数，并根据规则设置临时状态：
        当前死细胞（0）将在下一状态复活时，标记为2。
        当前活细胞（1）将在下一状态死亡时，标记为3。
        当前死细胞保持死亡或当前活细胞保持存活时，分别保持0或1。
        在第二次遍历网格时，将临时状态转换回最终状态：
        标记为2的转换为1（复活）。
        标记为3的转换为0（死亡）。
        """
        if not board or not board[0]:
            return
        # 定义好8个方向
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, 1), (1, 1), (-1, -1), (1, -1)]
        # 定义矩阵行m，列n
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                # 记录周围活细胞个数
                count = 0
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        if board[x][y] == 1 or board[x][y] == 3:
                            count += 1
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 3
                else:
                    if count == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0


print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
