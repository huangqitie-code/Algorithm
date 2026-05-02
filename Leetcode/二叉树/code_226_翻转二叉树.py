# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 题目链接:https://leetcode.cn/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    # 方法一 递归
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root

    # 方法二 迭代
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
