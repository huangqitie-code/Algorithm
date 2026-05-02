# 题目链接:https://leetcode.cn/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def intToRoman(self, num: int) -> str:
        val_symbols = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        ans=[]
        for symbol, value in val_symbols:
            while num >= symbol:
                num -= symbol
                ans.append(value)
            if num == 0:
                break
        return ''.join(ans)

