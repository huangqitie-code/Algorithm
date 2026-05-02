from typing import List


# 题目链接:https://leetcode.cn/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ans = strs[0]
        # 选取第一个元素作为参照物 遍历比较就行 结束条件就是发现有对应位置不相等
        # 或者长度不够
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                n = len(strs[j])
                if n-1<i or strs[0][i] != strs[j][i]:
                    return ans[:i]
        return ans
