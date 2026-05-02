# 题目链接:https://leetcode.cn/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isHappy(self, n: int) -> bool:
        setting = set()
        while n != 1:
            setting.add(n)
            # 获取每个位置的值先使用转str的
            s = str(n)
            s_sum = 0
            # for i in range(len(s)):
            #     a = ord(s[i]) - ord('0')
            #     s_sum += a ** 2
            # 使用除法
            while n > 0:
                a = n % 10
                n = n // 10
                s_sum += a * a
            n = s_sum
            if s_sum in setting:
                return False
        return True


print(Solution().isHappy(19))
