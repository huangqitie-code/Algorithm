# 题目链接:https://leetcode.cn/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 使用哈希表存储 时间复杂度O(n) 空间复杂度O(n)
        # map={}
        # for num in nums:
        #     if num in map:
        #         map[num] += 1
        #     else:
        #         map[num] = 1
        # for i in map:
        #     if map[i]>len(nums)/2:
        #         return i
        # return -1
        # 摩尔投票法 时间复杂度O(n) 空间复杂度O(1)
        # 思想大致就是遇到相同的元素就count + 1, 遇到不同的就count - 1表示抵消了
        # 假如存在出现次数大于n / 2的数肯定会到最后
        count = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                num = nums[i]
                count = 1
        return num


so = Solution()
print(so.majorityElement([3, 2, 3]))
print(so.majorityElement([2, 2, 1, 1, 1, 2, 2]))
