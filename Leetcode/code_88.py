from typing import List


# 题目链接:https://leetcode.cn/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 读题后知道这是归并排序的一部分
        # 不过这个题要不使用其他数组 直接原地操作
        # 所以需要从大到小排序且要从num1末尾开始排序
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


so = Solution()
so.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
so.merge([1], 1, [], 0)
so.merge([0], 0, [1], 1)
