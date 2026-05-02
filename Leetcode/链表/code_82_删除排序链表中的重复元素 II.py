from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 题目链接:https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and x == cur.next.val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
