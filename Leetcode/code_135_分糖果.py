from typing import List

# 题目链接:https://leetcode.cn/problems/candy/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if candy[i] <= candy[i + 1]:
                    candy[i] = candy[i + 1] + 1
        return sum(candy)
