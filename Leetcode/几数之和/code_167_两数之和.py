from typing import List


# 题目链接:https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 定义一个map记录每个数的位置
        # 此解法空间复杂度并不是O(1) 而是O(n)
        # 严格来讲不符合题目含义
        # dit = {}
        # lst = []
        # for i in range(len(numbers)):
        #     if target - numbers[i] in dit:
        #         lst.append(dit[target - numbers[i]] + 1)
        #         lst.append(i + 1)
        #         break
        #     dit[numbers[i]] = i
        # return lst
        # 双指针解法（数组是递增的所以可以用）
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1, j+1]
            elif s > target:
                j -= 1
            else:
                i += 1
        return [-1,-1]





print(Solution().twoSum([2, 3, 4], 6))
