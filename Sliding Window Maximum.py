class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller values from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append max once the first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
