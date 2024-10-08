class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        l, r = [1] * n, [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]
        res = []
        for i in range(n):
            res.append(l[i] * r[i])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    print(s.productExceptSelf(nums))
