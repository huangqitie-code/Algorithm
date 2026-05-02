# 题目链接:https://leetcode.cn/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 关键在于理解z字形首尾节点的刷新
        '''
        特殊情况处理：如果行数为1或字符串长度小于等于行数，直接返回原字符串。
        确定周期：每个Z字形排列的周期长度为2 * numRows - 2。
        逐行处理：遍历每一行，对于每个周期内的字符，根据其位置确定其在结果字符串中的位置：
        首行和末行每个周期只包含一个字符。
        中间行每个周期包含两个字符，第二个字符的位置可以通过计算周期和当前行数得出。
        '''
        if numRows == 1 or len(s) <= numRows:
            return s
        circle = 2 * numRows - 2
        ans = []
        for i in range(numRows):
            for j in range(i, len(s), circle):
                ans.append(s[j])
                if i != 0 and i != numRows - 1:
                    pos = j + circle - 2 * i
                    if pos < len(s):
                        ans.append(s[pos])
        return ''.join(ans)
so=Solution()
so.convert("PAYPALISHIRING",3)
