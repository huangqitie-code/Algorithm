from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 题目链接:https://leetcode.cn/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        left_prev = dummy
        for _ in range(left - 1):
            left_prev = left_prev.next
        start = left_prev.next
        end = left_prev.next
        while right - left > 0:
            right -= 1
            end = end.next
        right_last = end.next
        end.next = None
        left_prev.next = None

        pre = None
        cur = start

        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        left_prev.next = pre
        start.next = right_last
        return dummy.next


list1 = ListNode(5)
list1.next = ListNode(3)
Solution().reverseBetween(list1, 1, 2)
