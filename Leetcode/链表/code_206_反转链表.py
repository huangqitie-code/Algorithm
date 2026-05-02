from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 题目链接:https://leetcode.cn/problems/reverse-linked-list/description/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 方法一 递归实现
        # 递归函数就是返回链表反转后的节点
        # ans = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return ans
        # 方法二 迭代
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
