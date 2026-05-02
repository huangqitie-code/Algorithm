# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional

# 题目链接:https://leetcode.cn/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    # 这表示 head 可以是 ListNode 实例，也可以是 None
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        # 使用快慢指针 有环的话两者一定会相遇
        # 简单理解下 两者都在环内时候
        # 假设初始二者相差t步 那么经过t时刻二者就会相遇
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
