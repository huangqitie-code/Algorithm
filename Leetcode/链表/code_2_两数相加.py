from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 题目链接:https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 一开始写的 很粗糙能过
        dummy = ListNode(-1)
        ans = dummy
        mod = 0
        while l1 and l2:
            a, b = l1.val, l2.val
            n = (a + b + mod) % 10
            ans.next = ListNode(n)
            ans = ans.next
            mod = (a + b + mod) // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            a = l1.val
            n = (a + mod) % 10
            ans.next = ListNode(n)
            ans = ans.next
            mod = (a + mod) // 10
            l1 = l1.next
        while l2:
            a = l2.val
            n = (a + mod) % 10
            ans.next = ListNode(n)
            ans = ans.next
            mod = (a + mod) // 10
            l2 = l2.next
        if mod == 1:
            ans.next = ListNode(1)
        return dummy.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        # 表示进位
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            cur.next = ListNode((a + b + carry) % 10)
            cur = cur.next
            carry = (a + b + carry) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
