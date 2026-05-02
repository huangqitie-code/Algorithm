from typing import List


# 题目链接:https://leetcode.cn/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 排完序真的不要太简单 从高到低枚举最合适的H 找到就结束
        citations.sort()
        ans = len(citations)
        for i in range(len(citations)):
            if citations[i] >= ans:
                break
            else:
                ans -= 1
        return ans
