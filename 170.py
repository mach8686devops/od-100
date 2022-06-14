# 磁盘容量排序
import re

base = ("\dM", "\dG", "\dT")


def toM(s):
    total = 0
    for i, v in enumerate(base):
        d = re.search(v, s)
        if d:
            total += int(d.group()[:-1]) * 1000 ** i
    return total, s


while 1:
    try:
        n = int(input())

        nums = []
        for _ in range(n):
            # 将磁盘容量 M， G， T 全部转换为 M
            nums.append(toM(input()))

        nums = sorted(nums, key=lambda x: x[0])
        for d in nums:
            print(d[1])

    except Exception as e:
        break
