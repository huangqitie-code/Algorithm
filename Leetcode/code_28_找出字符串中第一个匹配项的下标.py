# 题目链接:https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 纯模拟很基础 不会就真的是代码能力太弱了
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
