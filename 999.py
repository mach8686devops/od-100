# 不定行的输入
# import sys
#
# res = []
# s = sys.stdin.readline().strip("\n")
# while s != "":
#     s = list(map(int, s.split()))
#     res.append(s)
#     s = sys.stdin.readline().strip("\n")
#
# print(res)

from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        while len(nums) > 1:
            nums = [min(nums[2 * i], nums[2 * i + 1]) if i & 1 == 0 else max(nums[2 * i], nums[2 * i + 1]) for i in
                    range(0, int(len(nums) // 2))]
        return nums[0]


# print(Solution().minMaxGame(nums=[1, 3, 5, 2, 4, 8, 2, 2]))


class Solution2303:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        nums = [i[0] for i in brackets]
        taxs = [i[1] for i in brackets]
        maxi = max(nums)
        mini = min(nums)
        ans = 0.00
        for i,val in enumerate(nums):
            if i==0 and nums[0] < income:
                ans += (nums[0]-0)*taxs[0]/100
                # print(ans)
            if i==0 and nums[0]>=income:
                ans += (nums[0]-income)*taxs[0]/100
                return ans
            if i>=1 and val < income:
                ans += (val-nums[i-1])*taxs[i]/100
                # print(ans)
            elif i>=1 and val >= income:
                ans += (income-nums[i-1])*taxs[i]/100
                # print(ans)
                return ans
        return ans

print(Solution2303().calculateTax(brackets=[[10,10]], income=5))