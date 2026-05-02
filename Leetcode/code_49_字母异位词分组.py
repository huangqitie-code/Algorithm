from collections import defaultdict
from typing import List


# 题目链接:https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 该方法时间复杂度有点高O(n²)
        # def isAnagram(s: str, t: str) -> bool:
        #     if len(s) != len(t):
        #         return False
        #     mapping = {}
        #     for c in s:
        #         mapping[c] = mapping.get(c, 0) + 1
        #     for c in t:
        #         if c not in mapping:
        #             return False
        #         if mapping[c] < 1:
        #             return False
        #         mapping[c] -= 1
        #     return True
        # if not strs:
        #     return [[]]
        # ans = []
        # index = []
        # for i in range(len(strs)):
        #     if i in index:
        #         continue
        #     lst = [strs[i]]
        #     for j in range(i + 1, len(strs)):
        #         if isAnagram(strs[i], strs[j]):
        #             lst.append(strs[j])
        #             index.append(j)
        #     ans.append(lst)
        # return ans
        # 方法二 时间复杂度O(n*k)k为字符串的平均长度
        # 很好的一个库函数 自动处理键不存在的情况 list是定义值的类型
        groups = defaultdict(list)
        for s in strs:
            # 字母计数
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # key必须为不可变对象 这里可以为tuple或者str
            key = tuple(count)
            print(key)
            groups[key].append(s)
        return list(groups.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))