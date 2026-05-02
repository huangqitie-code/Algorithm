class Solution:
    # 题目链接:https://leetcode.cn/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_str = s.split(" ")
        print(word_str)
        if len(word_str) != len(pattern):
            return False
        mapping = {}
        for i in range(len(pattern)):
            pi = pattern[i]
            wi = word_str[i]
            if pi not in mapping:
                if wi not in mapping.values():
                    mapping[pi] = wi
                else:
                    return False
            else:
                if wi != mapping[pi]:
                    return False
        return True


print(Solution().wordPattern("abba", "dog dog dog dog"))
