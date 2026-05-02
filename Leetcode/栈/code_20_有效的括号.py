# 题目链接:https://leetcode.cn/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            # 如果是右括号
            if char in mapping:
                # stack为空或者不配对弹出栈顶元素不匹配
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                # 左括号入栈
                stack.append(char)
        # 如果栈为空，则所有括号都匹配成功
        return not stack

    def isValid2(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif not stack or stack.pop() != char:
                return False
        return not stack

print(Solution().isValid2('([])'))
