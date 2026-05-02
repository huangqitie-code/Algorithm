# 题目链接:https://leetcode.cn/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [c.lower() for c in s if c.isalnum()]
        return ''.join(lst) == ''.join(lst[::-1])
