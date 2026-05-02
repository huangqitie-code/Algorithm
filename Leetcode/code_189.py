from typing import List


# 题目链接:https://leetcode.cn/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        if nums is None or k % len(nums) == 0 or len(nums) == 1:
            return
        n = len(nums)
        k %= n

        # 最简单的方法 分割两个数据 时间复杂度O(n) 空间复杂度O(n)
        # k = k % n
        # left = nums[0: - k]
        # right = nums[- k:]
        # nums[:] = right + left

        # 三个部分进行翻转 时间复杂度O(n) 空间复杂度O(1)
        # 1.翻转整个数组
        # 2.翻转0到k部分
        # 3.翻转k到n-1部分
        def reverse(nums: List[int], left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        print(nums)


so = Solution()
so.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
