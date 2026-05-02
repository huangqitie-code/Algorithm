from typing import List


# 题目链接:https://leetcode.cn/problems/4sum/description/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        if l < 4:
            return []
        nums.sort()
        ans = []
        # 定二移二
        for i in range(l - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, l - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                m, n = j + 1, l - 1
                while m < n:
                    total = nums[i] + nums[j] + nums[m] + nums[n]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[m], nums[n]])
                        while m < n and nums[m] == nums[m + 1]:
                            m += 1
                        while m < n and nums[n] == nums[n - 1]:
                            n -= 1
                        m += 1
                        n -= 1
                    elif total < target:
                        while m < n and nums[m] == nums[m + 1]:
                            m += 1
                        m += 1
                    else:
                        while m < n and nums[n] == nums[n - 1]:
                            n -= 1
                        n -= 1
        return ans
Solution().fourSum([-1, 0, 1, 2, -1, -4],0)
