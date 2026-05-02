from typing import List


# 题目链接:https://leetcode.cn/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 法一使用map空间复杂度O(n)
        # mapping = {}
        # for i,num in enumerate(nums):
        #     if num in mapping and i - mapping[num] <= k:
        #             return True
        #     mapping[num] = i
        # return False
        # 法二 使用set 只保留k个值 空间复杂度O(k)
        num_set = set()
        for i, num in enumerate(nums):
            if num in num_set:
                return True
            num_set.add(num)
            if len(num_set) > k:
                num_set.remove(nums[i - k])
        return False


print(Solution().containsNearbyDuplicate([1, 2, 2, 3], 2))
