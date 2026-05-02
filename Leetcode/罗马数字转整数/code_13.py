# 题目链接:https://leetcode.cn/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        遍历罗马数字字符串，对于每个字符，将其对应的数值加到总和中。
        如果当前字符的数值大于前一个字符的数值，说明遇到了特殊情况，
        需要减去前一个字符数值的两倍（因为前一个字符已经被错误地加上了一次）。
        时间复杂度为O(n)，空间复杂度为O(1)
        '''
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        prev_value = 0
        for c in s:
            current_value = roman_dict[c]
            ans += current_value
            if current_value > prev_value:
                ans-=2*prev_value
            prev_value = current_value
        return ans
