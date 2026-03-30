class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        mp = {}

        # Precompute all substring values up to length 30
        for i in range(n):
            if s[i] == '0':
                # special case: "0" -> value 0
                if 0 not in mp:
                    mp[0] = (i, i)
                continue
            
            val = 0
            for j in range(i, min(n, i + 30)):
                val = (val << 1) | (ord(s[j]) - ord('0'))
                
                if val not in mp:
                    mp[val] = (i, j)

        # Process queries
        ans = []
        for first, second in queries:
            target = first ^ second
            if target in mp:
                ans.append(list(mp[target]))
            else:
                ans.append([-1, -1])

        return ans
