from typing import List


# 题目链接:https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                if token == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                if token == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                if token == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                if token == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack.pop()


print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
