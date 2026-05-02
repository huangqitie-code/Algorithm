# 题目链接:https://leetcode.cn/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseWords(self, s: str) -> str:
        # 双指针
        ans = []
        k = len(s) - 1
        begin = 0
        # 一种做法去掉前导空格
        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         begin = i
        #         break
        # while k >= begin:
        #     j = k
        #     while j >= 0 and s[j] == ' ':
        #         j -= 1
        #     i = j
        #     while i >= 0 and s[i] != ' ':
        #         i -= 1
        #     k = i
        #     ans.append(s[i + 1:j + 1])
        # 第二种做法就是追加判断不为空格
        while k >= 0:
            j = k
            while j >= 0 and s[j] == ' ':
                j -= 1
            i = j
            while i >= 0 and s[i] != ' ':
                i -= 1
            k = i
            # 判断不为空格再追加
            if s[i+1:j+1]:
                ans.append(s[i + 1:j + 1])
        return ' '.join(ans)

so=Solution()
so.reverseWords("the sky is blue")

