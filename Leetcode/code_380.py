# 题目链接:https://leetcode.cn/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
import random


class RandomizedSet:


    def __init__(self):
        self.lst = []
        self.dic = {}

    # 为了实现一个支持快速插入、删除和随机访问的集合，我们可以结合哈希表和动态数组的优势。
    # 哈希表用于快速判断元素是否存在，并记录元素的索引，而动态数组用于存储元素，以便快速随机访问。
    # 删除操作时，将待删除元素与数组末尾元素交换，再删除末尾元素，以保持时间复杂度为O(1)。
    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.lst.append(val)
            self.dic[val] = len(self.lst) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        n = len(self.lst)
        if val in self.dic:
            valindex = self.dic[val]
            num = self.lst[n-1]
            # 将列表目标元素位置的值直接替换成最后一位的值
            # 在字典中更新最后一位的索引
            # 然后删除最后一位即可
            self.lst[valindex] = num
            self.dic[num] = n-1
            # del self.dic[val]
            self.dic.pop(val)
            self.lst.pop()
            # del self.lst[n - 1]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.lst)


randomizedSet = RandomizedSet()
randomizedSet.insert(1)
randomizedSet.remove(2)
randomizedSet.insert(2)
randomizedSet.getRandom()
randomizedSet.remove(1)
randomizedSet.insert(2)
randomizedSet.getRandom()
