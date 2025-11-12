from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        res = []
        p_count = Counter(p)           
        window_count = Counter(s[:m])  

        if window_count == p_count:
            res.append(0)

        for i in range(m, n):
            left_char = s[i - m]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            right_char = s[i]
            window_count[right_char] += 1

            if window_count == p_count:
                res.append(i - m + 1)

        return res
