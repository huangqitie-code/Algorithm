from typing import List


# 题目链接:https://leetcode.cn/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        need = [0] * 128
        for i in p:
            need[ord(i)] += 1
        # 继续初始化窗口
        left, right = 0, 0
        # 总共需要匹配上的总字符数
        total = len(p)
        ans = []
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
                if right - left + 1 == len(p):
                    ans.append(left)
                # 以当前left为起点最小的长度已得到 往后走一个继续扩展右边界
                # 等待下次total等于0进行长度的更新
                total += 1
                need[ord(s[left])] += 1
                left += 1
            right += 1
        return ans
