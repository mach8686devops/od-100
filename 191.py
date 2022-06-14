# 字符统计及重排】
# 【字符统计及重排】给出⼀个仅包含字⺟的字符串，不包含空格，统计字符串中各个字⺟（区分⼤⼩写）出现的次数，并按照字⺟出现次数从⼤到⼩的顺序输出各个
# 字⺟及其出现次数。如果次数相同，按照⾃然顺序进⾏排序，且⼩写字⺟在⼤写字⺟之前。
# 输⼊描述：
#
# 输⼊⼀⾏，为⼀个仅包含字⺟的字符串。
#
# 输出描述：
#
# 按照字⺟出现次数从⼤到⼩的顺序输出各个字⺟和字⺟次数，⽤英⽂分号分隔，注意末尾的分号；字⺟和次数间⽤英⽂冒号分隔。
#
# 示例1：
# 输入
#
# xyxyXX
#
# 输出
#
# x:2;y:2;X:2
# ————————————————
# 版权声明：本文为CSDN博主「@_南先森」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/nanzhanfei/article/details/124895671


while 1:
    try:
        strs = input()
        from collections import Counter

        ans = dict(Counter(strs))
        # print(ans)
        ant = ""
        for m, n in ans.items():
            ant += str(m)
            ant += str(n)
            ant += ";"
        print(ant[:-1])
    except Exception as e:
        print(e)
        break
