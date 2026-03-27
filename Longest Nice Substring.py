class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(sub):
            if len(sub) < 2:
                return ""
            
            char_set = set(sub)
            
            for i, c in enumerate(sub):
                if c.lower() not in char_set or c.upper() not in char_set:
                    left = helper(sub[:i])
                    right = helper(sub[i+1:])
                    
                    return left if len(left) >= len(right) else right
            
            return sub
        
        return helper(s)
