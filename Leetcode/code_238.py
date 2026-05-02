from typing import List


# 题目链接:https://leetcode.cn/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    '''
    0-i乘积和i到n-1乘积的关系

    laim[i] 表示0到i-1的乘积

    laim[0]=1

    laim[1]=nums[0]=1

    laim[2]=nums[0]*nums[1]=2

    laim[3]=nums[0]*nums[1]*nums[2]=6

    laim[n-1]=nums[0]*nums[1]*...nums[n-2]

    ...

    Raim[i]表示i+1到n-1的乘积

    raim[n-1]=1

    raim[n-2]=nums[n-1]=4

    raim[n-3]=nums[n-1]*nums[n-2]=12

    ...
    i laim[i]是0-i-1的乘积 raim[i]是i+1到n-1的乘积

    ans[i]=laim[i]*raim[i]
    '''

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        # 做法一时间复杂度O(n),空间复杂度O(n)
        # laim = [1] * n
        # raim = [1] * n
        # for i in range(1, n):
        #     laim[i] = laim[i - 1] * nums[i - 1]
        #     raim[n - 1 - i] = raim[n - i] * nums[n - i]
        # for i in range(n):
        #     ans[i] = laim[i] * raim[i]
        # 做法二时间复杂度O(n),空间复杂度O(1)
        left, right = 1, 1
        for i in range(n):
            ans[i] *= left
            ans[n - 1 - i] *= right
            left *= nums[i]
            right *= nums[n - 1 - i]
        return ans


print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
