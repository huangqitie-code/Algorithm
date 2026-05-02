from typing import List


# 题目链接:https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        直觉：使用哈希集合来存储所有数字，以便快速查找。对于每个数字，检查它是否是某个连续序列的起点（即前一个数字不存在于集合中）。如果是起点，则向后检查连续的数字是否存在，统计序列长度。
        算法选择：利用集合来存储数字，遍历每个数字，仅当数字是序列起点时进行连续检查，确保每个数字最多被处理两次，从而实现 O(n) 的时间复杂度。
        复杂度分析：每个数字最多被访问两次（一次在遍历中，一次在连续检查中），因此总时间复杂度为 O(n)。空间复杂度为 O(n) 用于存储数字集合。
        '''
        num_set = set(nums)
        ans = 0
        for num in num_set:
            # 如果num-1不在集合 说明num可以作为起点进行检查
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                ans = max(ans, current_streak)
        return ans

