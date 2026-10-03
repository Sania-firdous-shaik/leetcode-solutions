class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans, n = 0, len(s)
        for t in range(1, 27):
            freq = [0] * 26
            u = valid = left = 0
            for right in range(n):
                r_idx = ord(s[right]) - 97
                if freq[r_idx] == 0:
                    u += 1
                if freq[r_idx] == k - 1:
                    valid += 1
                freq[r_idx] += 1
                while u > t:
                    l_idx = ord(s[left]) - 97
                    if freq[l_idx] == 1:
                        u -= 1
                    if freq[l_idx] == k:
                        valid -= 1
                    freq[l_idx] -= 1
                    left += 1
                if u == t and valid == u:
                    ans = max(ans, right - left + 1)
        return ans