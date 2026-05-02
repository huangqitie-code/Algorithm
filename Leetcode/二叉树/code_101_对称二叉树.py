# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 题目链接:https://leetcode.cn/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    # 方法一 递归
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        if root is None:
            return True
        return isMirror(root.left, root.right)

    # 方法二 迭代使用队列
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queue.append(left.right)
            queue.append(right.left)
            queue.append(left.left)
            queue.append(right.right)
        return True

    # 方法三 迭代使用栈
    def isSymmetric3(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            stack.append(left.right)
            stack.append(right.left)
            stack.append(left.left)
            stack.append(right.right)
        return True

