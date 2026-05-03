class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res

    #Mine, much worse:
    m = sum(nums[n] * n for n in range(0, len(nums)))
        fk = m
        k, carry, l = 1, sum(nums[:len(nums)-1]), len(nums)
        while k < l:
            fk = (fk + carry) - ((nums[l - k] * (l - 1)))
            carry = (carry + nums[l - k]) - (nums[l - k - 1])
            m = max(m, fk)
            k += 1
        return m
