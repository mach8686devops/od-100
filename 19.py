#!/usr/bin/python
# -*- coding: utf-8 -*-

# 给定一个随机的整数（可能存在正整数和负整数）数组 nums ，请你在该数组中找出两个数，其和的绝对值(|nums[x]+nums[y]|)为最小值，并返回这个两个数（按从小到大返回）以及绝对值。
# 每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# 输入描述:
#
# 一个通过空格分割的有序整数序列字符串，最多1000个整数，且整数数值范围是 [-65535, 65535]。
#
# 输出描述:
#
# 两数之和绝对值最小值
#
# 示例1
#
# 输入
#
# -1 -3 7 5 11 15
#
# 输出
#
# -3 5 2
# ————————————————
# 版权声明：本文为CSDN博主「@_南先森」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/nanzhanfei/article/details/124895671
while 1:
    try:
        nums = sorted(input().split(" "))
        sum_dict = {}
        minsum = -1
        for x in range(0, len(nums) - 1):
            for y in range(x + 1, len(nums)):
                sum = abs(int(nums[x]) + int(nums[y]))
                if minsum == -1 or sum < minsum:
                    minsum = sum
                    numx = nums[x]
                    numy = nums[y]
                    if numx > numy:
                        numx, numy = numy, numx
        print(numx, numy, minsum)
    except Exception as e:
        break

# -3 -1 5 9 17
# -3 5 2
# -3 -1 1 5 7
# -1 1 0
