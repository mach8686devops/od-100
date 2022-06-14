# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter
from typing import List


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

while 1:
    try:
        import sys
        for line in sys.stdin:
            a = line.replace("\n", "").split(",")
            n = int(sys.stdin.readline().strip())
            # print(a)
            ans = {}
            for item in a:
                if "-" in item:
                    ans[int(item.split("-")[0])] = item
                else:
                    ans[int(item)]=item
            # print(a, ans)
            keys = list(ans.keys())
            keys.sort()
            vals =[]
            for key in keys:
                vals.append(ans[key])
            print(keys, vals, n)
            m = len(keys)
            if n in keys:
                vals.remove(str(n))
            else:
                # print(keys)

                for i, val, yy in zip(list(range(m)), keys, vals):
                    # print(i, val, yy)
                    res = ""
                    ant = yy.split("-")
                    # print(ant)
                    list_ant = list(range(int(ant[0]), int(ant[1])+1))
                    if n in list_ant:
                        list_ant.remove(n)
                    for i, val in enumerate(list_ant):
                        j=1
                        while j< len(list_ant)-1-i:
                            if list_ant[i]+j == list_ant[i+j]:
                                j +=1
                            else:
                                break
                    if j==1:
                        res += list_ant[0]
                        res += ','



                    print(list_ant)
            print(vals)


    except Exception as e:
        pass




# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
