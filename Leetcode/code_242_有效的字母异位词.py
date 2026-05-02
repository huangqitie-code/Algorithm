# 题目链接:https://leetcode.cn/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        for c in s:
            mapping[c] = mapping.get(c, 0) + 1
        for c in t:
            if c not in mapping:
                return False
            if mapping[c] < 1:
                return False
            mapping[c] -= 1
        return True


print(Solution().isAnagram("rat", "car"))
