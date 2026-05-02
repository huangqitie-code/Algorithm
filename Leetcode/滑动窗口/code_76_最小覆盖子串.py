# 题目链接:https://leetcode.cn/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # need = defaultdict(int)
        need = [0] * 128
        for i in t:
            need[ord(i)] += 1
        # 继续初始化窗口
        left, right = 0, 0
        # 总共需要匹配上的总字符数
        total = len(t)
        begin = 0
        ans = len(s) + 1  # 这里也可以是float('inf')
        while right < len(s):
            if need[ord(s[right])] > 0:
                total -= 1
            need[ord(s[right])] -= 1
            # 匹配完了 判断是否还多了
            if total == 0:
                while need[ord(s[left])] < 0:
                    need[ord(s[left])] += 1
                    left += 1
                # 不能再往前缩了就停止
                if right - left + 1 < ans:
                    ans = right - left + 1
                    begin = left
                # 以当前left为起点最小的长度已得到 往后走一个继续扩展右边界
                # 等待下次total等于0进行长度的更新
                # total += 1
                # need[ord(s[left])] += 1
                # left += 1
            right += 1
        return "" if ans == (len(s) + 1) else s[begin:begin + ans]


print(Solution().minWindow("ADOBECODEBANCDDDABC", "ABC"))
