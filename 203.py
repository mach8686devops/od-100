# 一只顽猴想要从山脚爬到山顶
#   途中经过一个有n个台阶的阶梯，但是这个猴子有个习惯，每一次只跳1步或3步
#   试问？猴子通过这个阶梯有多少种不同的跳跃方式
#
#   输入描述：
#     输入只有一个这个数n    0<n<50
#     此阶梯有多个台阶
#   输出描述：
#     有多少种跳跃方式
#
#   实例:
#    输入
#      50
#    输出
#       122106097
#
#    输入
#       3
#    输出
#       2

while 1:
    try:
        n = int(input())

        from functools import lru_cache


        @lru_cache(100)
        def func(n):
            if 0 <= n <= 3:
                return [0, 1, 1, 2][n]
            elif n >= 4:
                return func(n - 3) + func(n - 1)


        print(func(n))
    except Exception as e:
        print(e)
        break
