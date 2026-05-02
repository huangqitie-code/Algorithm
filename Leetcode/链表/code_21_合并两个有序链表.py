# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 题目链接:https://leetcode.cn/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 归并排序核心思想
        if list1 is None and list2 is None:
            return None
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next
def linked_list_to_list(head):
    """将链表转换为列表"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
print(linked_list_to_list(Solution().mergeTwoLists(list1, list2)))
