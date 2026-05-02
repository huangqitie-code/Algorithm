from typing import Optional


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


# 题目链接:https://leetcode.cn/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 字节很喜欢的面试题
        # 方法一 使用map存储节点key->旧节点 value->新节点
        if not head:
            return None
        mapping = {}
        cur = head
        # 先存储节点
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 将新节点串起来
        while cur:
            mapping[cur].next = mapping[cur.next] if cur.next else None
            mapping[cur].random = mapping[cur.random] if cur.random else None
            cur = cur.next
        return mapping[head]

    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 常数空间的解法
        # A->A'->B->B'->C->C'
        if not head:
            return None
        # 第一步 插入A'、B'、C'
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = node.next
        # 第二步 设置随机指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next
        # 抽取A'、B'、C'出来返回
        old_list = head
        new_list = head.next
        ans = head.next
        while old_list:
            old_list.next = old_list.next.next
            if new_list.next:
                new_list.next = new_list.next.next
            else:
                new_list.next = None
            old_list = old_list.next
            new_list = new_list.next
        return ans
