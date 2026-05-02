from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 题目链接:https://leetcode.cn/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 定义翻转链表方法
        def reverse(a, b):
            pre = None
            cur = a
            while cur != b:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        # 一次丢k个进去翻转
        a = head
        b = head
        for i in range(k):
            if not b:
                return head
            b = b.next
        ans = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return ans
