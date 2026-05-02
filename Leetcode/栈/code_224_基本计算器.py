# 题目链接:https://leetcode.cn/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def calculate(self, s: str) -> int:
        """
        初始化栈ops为[1]，初始符号sign为1，结果ans为0。
        遍历字符串：
        跳过空格。
        遇到'+'：设置sign为栈顶符号（表示当前层的符号）。
        遇到'-'：设置sign为负的栈顶符号（处理一元负号）。
        遇到'('：将当前sign压入栈（进入新括号层）。
        遇到')'：弹出栈顶符号（退出当前括号层）。
        遇到数字：读取连续数字字符，计算数字值，并加上sign * num到结果。
        """
        ops = [1]  # 栈用于存储每层的符号，初始为1（正号）
        sign = 1  # 当前符号，1表示正，-1表示负
        ans = 0  # 累计结果
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]  # 设置当前符号为栈顶符号
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]  # 设置当前符号为负的栈顶符号（处理一元负号）
                i += 1
            elif s[i] == '(':
                ops.append(sign)  # 进入新括号层，当前符号压栈
                i += 1
            elif s[i] == ')':
                ops.pop()  # 退出当前括号层，弹出栈顶符号
                i += 1
            else:
                # 读取连续数字字符
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ans += sign * num  # 将数字与当前符号相乘后累加到结果
        return ans

    def calculate2(self, s: str) -> int:
        # 递归实现
        i = 0  # 使用闭包变量跟踪索引位置
        def evaluate():
            nonlocal i  # 引用闭包作用域外层函数中的变量与global(全局)要区分开
            result = 0
            current_sign = 1
            while i < len(s):
                char = s[i]
                if char == ' ':
                    i += 1
                    continue
                if char == '+':
                    current_sign = 1
                    i += 1
                elif char == '-':
                    current_sign = -1
                    i += 1
                elif char == '(':
                    i += 1  # 跳过 '('
                    sub_result = evaluate()  # 递归处理子表达式
                    result += current_sign * sub_result
                elif char == ')':
                    i += 1  # 跳过 ')'
                    return result  # 返回当前层级的结果
                else:
                    # 处理数字
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    result += current_sign * num
            return result

        return evaluate()
    # 或者定义的方法在外层 使用self.i来记录访问的位置
    def calculate3(self, s: str) -> int:
        self.i = 0
        return self.evaluate(s)

    def evaluate(self, s: str) -> int:
        result = 0
        current_sign = 1
        while self.i < len(s):
            char = s[self.i]

            if char == ' ':
                self.i += 1
                continue
            if char == '+':
                current_sign = 1
                self.i += 1
            elif char == '-':
                current_sign = -1
                self.i += 1
            elif char == '(':
                self.i += 1
                sub_result = self.evaluate(s)
                result += current_sign * sub_result
                # 移除了重置符号的操作
            elif char == ')':
                self.i += 1
                return result
            else:
                num = 0
                while self.i < len(s) and s[self.i].isdigit():
                    num = num * 10 + int(s[self.i])
                    self.i += 1
                result += current_sign * num
        return result


print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
