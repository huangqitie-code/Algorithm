from typing import List


# 题目链接:https://leetcode.cn/studyplan/top-interview-150/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        方法思路
        总油量检查：首先，我们需要确保所有加油站的油量总和大于等于消耗总和。如果总油量不足，汽车显然无法绕行一周，直接返回-1。
        贪心算法：在总油量足够的情况下，我们可以使用贪心算法来找到起始点。遍历每个加油站，维护当前油量。如果当前油量为负，说明之前的起点无法绕行，将起点设为下一个加油站，并重置当前油量。最终找到的起点即为答案。
        这个算法需要想明白为啥中间的起始点不行 这里参考官方题解有说明
        '''
        start = 0
        n = len(gas)
        current_gas = 0
        total_gas = 0
        for i in range(n):
            current_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        return start if total_gas >= 0 else -1
