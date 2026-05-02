# 题目链接:https://leetcode.cn/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('')
        stack = []
        for part in parts:
            if part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)


print(Solution().simplifyPath('/home/'))
