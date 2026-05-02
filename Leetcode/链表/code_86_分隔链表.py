from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 题目链接：https://leetcode.cn/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 初始化两个链表
        small_node = ListNode(0)
        big_node = ListNode(0)
        cur = head
        small_cur = small_node
        big_cur = big_node
        while cur:
            if cur.val < x:
                small_cur.next = cur
                small_cur = small_cur.next
            else:
                big_cur.next = cur
                big_cur = big_cur.next
            cur = cur.next
        small_cur.next = big_node.next
        big_cur.next = None
        return small_node.next





