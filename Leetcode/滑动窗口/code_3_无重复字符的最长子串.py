# 题目链接:https://leetcode.cn/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 老样子窗口初始化
        if not s:
            return 0
        left, right = 0, 0
        ans = 1
        st = set()
        while right < len(s):
            while s[right] in st:
                st.remove(s[left])
                left += 1
            st.add(s[right])
            right += 1
            ans = max(ans, right - left)
        return ans


print(Solution().lengthOfLongestSubstring("pwwkew"))