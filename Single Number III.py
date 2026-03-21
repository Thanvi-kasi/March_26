class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        
        # Step 1: XOR all elements
        for num in nums:
            xor ^= num
        
        # Step 2: Get rightmost set bit
        diff = xor & -xor
        
        # Step 3: Divide numbers into two groups
        a, b = 0, 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
