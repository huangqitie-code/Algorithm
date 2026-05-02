# 题目链接:https://leetcode.cn/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            # 检查s->t映射
            if s_char in mapping:
                if mapping[s_char] != t_char:
                    return False
            # 检查t->s映射（通过字典值匹配）
            else:
                # 检查t_char是否已被其他字符映射
                if t_char in mapping.values():
                    return False
                mapping[s_char] = t_char
        return True

print(Solution().isIsomorphic('paper', 'title'))
