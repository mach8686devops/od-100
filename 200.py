# 全排列 无重复数字
import itertools


while 1:
    try:
        nums = list(map(int, input().split(",")))
        print([list(i) for i in itertools.permutations(nums, len(nums))])
    except Exception as e:
        break
