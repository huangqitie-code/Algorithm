from collections import defaultdict
from typing import List


# 题目链接:https://leetcode.cn/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_map = defaultdict(int)
        word_len = len(words[0])
        # 初始化每个单词 欠债表
        for i in range(len(words)):
            words_map[words[i]] += 1
        ans = []
        # 类比438题 这里其实就是将多个字母看成一个单词来处理
        # 模板是一摸一样的
        # 要注意的就三点
        # 1.要遍历从(0,word_len)分别作为起点
        # 2.每次的跳跃间隔是word_len 而不是1了
        # 3.map和total内存循环完要记得更新成原来的
        for i in range(word_len):
            left, right = i, i
            total = len(words)
            # map浅拷贝
            words_use_map = defaultdict(int,dict(words_map))
            while right < len(s):
                if words_use_map[s[right:right + word_len]] > 0:
                    total -= 1
                words_use_map[s[right:right + word_len]] -= 1
                if total == 0:
                    while words_use_map[s[left:left + word_len]] < 0:
                        words_use_map[s[left:left + word_len]] += 1
                        left += word_len
                    if (right - left) / word_len + 1 == len(words):
                        ans.append(left)
                    total += 1
                    words_use_map[s[left:left + word_len]] += 1
                    left += word_len
                right += word_len
        return ans


print(Solution().findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]))
