from typing import List


# 题目链接:https://leetcode.cn/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ans = []
        # 三个指针固定左边后当成双指针来做
        for k in range(n - 2):
            if nums[k] > 0:
                break
            # 跳过重复值
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, n - 1
            while i < j:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    # 跳过重复值
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif total < 0:
                    # 跳过重复值
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    i += 1
                else:
                    # 跳过重复值
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    j -= 1
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
