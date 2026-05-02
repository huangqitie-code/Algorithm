from typing import Optional


# 题目链接：https://leetcode.cn/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 首先计算链表长度
        if not head or not head.next:
            return head
        n = 1
        cur = head
        while cur.next:
            n += 1
            cur = cur.next
        k = k % n
        if k == 0:
            return head
        new_cur = head
        for _ in range(n - k - 1):
            new_cur = new_cur.next
        new_head = new_cur.next
        new_cur.next = None
        cur.next = head
        return new_head



