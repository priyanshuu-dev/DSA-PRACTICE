from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        for c in t:
            freq_t[c] += 1

        low = 0
        have = 0
        need = len(freq_t)

        res_len = float('inf')
        res = ""

        for high in range(len(s)):
            freq_s[s[high]] += 1

            if s[high] in freq_t and freq_s[s[high]] == freq_t[s[high]]:
                have += 1

            while have == need:
                # update answer
                if (high - low + 1) < res_len:
                    res_len = high - low + 1
                    res = s[low:high+1]

                # shrink window
                freq_s[s[low]] -= 1

                if s[low] in freq_t and freq_s[s[low]] < freq_t[s[low]]:
                    have -= 1

                low += 1

        return res