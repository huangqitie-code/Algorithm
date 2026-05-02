from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 题目链接:https://leetcode.cn/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针 一次遍历完成
        dummy = ListNode(0, head)
        a = dummy
        b = dummy
        for i in range(n + 1):
            a = a.next
        while a:
            a = a.next
            b = b.next
        b.next = b.next.next
        return dummy.next
