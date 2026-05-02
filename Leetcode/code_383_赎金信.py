# 题目链接:https://leetcode.cn/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # wordMap = {}
        # for i in range(len(magazine)):
        #     if magazine[i] not in wordMap:
        #         wordMap[magazine[i]] = 1
        #     else:
        #         wordMap[magazine[i]] += 1
        # for i in range(len(ransomNote)):
        #     if ransomNote[i] not in wordMap:
        #         return False
        #     else:
        #         if wordMap[ransomNote[i]] == 0:
        #             return False
        #         else:
        #             wordMap[ransomNote[i]] -= 1
        # return True
        count = [0] * 26
        for i in range(len(magazine)):
            count[ord(magazine[i]) - ord('a')] += 1
        for i in range(len(ransomNote)):
            if count[ord(ransomNote[i]) - ord('a')] == 0:
                return False
            else:
                count[ord(ransomNote[i]) - ord('a')] -= 1
        return True


print(Solution().canConstruct(ransomNote='a', magazine='ab'))
