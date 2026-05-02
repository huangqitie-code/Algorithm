# 题目链接:https://leetcode.cn/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150
class MinStack:

    def __init__(self):
        self.stack = []
        # 栈顶始终是最小元素 其他元素不管
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    # 删除时如果是最小元素则需要同步删除最小栈的
    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None
