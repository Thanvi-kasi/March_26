class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        base = 26
        mod = 2**63 - 1

        def search(L):
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % mod

            seen = {h}
            baseL = pow(base, L, mod)

            for start in range(1, n - L + 1):
                h = (h * base - nums[start - 1] * baseL + nums[start + L - 1]) % mod
                if h in seen:
                    return start
                seen.add(h)
            return -1

        left, right = 1, n
        start = -1

        while left <= right:
            mid = (left + right) // 2
            idx = search(mid)
            if idx != -1:
                left = mid + 1
                start = idx
            else:
                right = mid - 1

        if start == -1:
            return ""
        return s[start:start + left - 1]
