from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 题目链接:https://leetcode.cn/problems/count-good-nodes-in-binary-tree/
def goodNodes(self,root: Optional[TreeNode]) -> int:
    # 用栈模拟递归
    # if not root:
    #     return 0
    # stack = [(root, root.val)]
    # count = 0
    # while stack:
    #     node, current_max = stack.pop()
    #     if node.val >= current_max:
    #         count += 1
    #         current_max = node.val
    #     if node.left:
    #         stack.append((node.left, current_max))
    #     if node.right:
    #         stack.append((node.right, current_max))
    # return count
    # 直接递归dfs深度优先
    self.ans = 0
    def dfs(root, pathMax):
        if root is None:
            return
        if root.val >= pathMax:
            self.ans += 1
            pathMax = root.val
        dfs(root.left, pathMax)
        dfs(root.right, pathMax)
    dfs(root, root.val)
    return self.ans


root = TreeNode(3)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
print(goodNodes(root))
