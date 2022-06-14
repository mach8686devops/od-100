# vlan资源池

# ***VLAN***是一种对局域网设备进行逻辑划分的技术，为了标识不同的VLAN，引入VLAN ID(1-4094之间的整数)的概念。
# 定义一个VLAN ID的资源池(下称VLAN资源池)，资源池中连续的VLAN用开始VLAN-结束VLAN表示，不连续的用单个整数表示，所有的VLAN用英文逗号连接起来。现
# 在有一个VLAN资源池，业务需要从资源池中申请一个VLAN，需要你输出从VLAN资源池中移除申请的VLAN后的资源池。
# 输入描述：
#
# 第一行为字符串格式的VLAN资源池，第二行为业务要申请的VLAN，VLAN的取值范围为[1,4094]之间的整数。
# 输出描述：
#
# 从输入VLAN资源池中移除申请的VLAN后字符串格式的VLAN资源池，输出要求满足题目描述中的格式，并且按照VLAN从小到大升序输出。
# 如果申请的VLAN不在原VLAN资源池内，输出原VLAN资源池升序排序后的字符串即可。
# 备注：
#
# 输入VLAN资源池中VLAN的数量取值范围为[2-4094]间的整数，资源池中VLAN不重复且合法([1,4094]之间的整数)，输入是乱序的。


def appends(ans, start, last):
    if start == last:
        ans.append(str(last))

    else:
        ans.append("-".join([str(start), str(last)]))


def main(input_str, request):
    ans = []
    sets = set()
    # 先转为 整数的列表（集合） 除去之后 再转回来
    for string in input_str.split(','):
        if "-" in string:
            ss = string.split("-")
            for i in range(int(ss[0]), int(ss[1]) + 1):
                sets.add(int(i))
        else:
            sets.add(int(string))
    # print(sets)
    # 尝试移除
    try:
        sets.remove(request)
    except KeyError:
        pass

    last = start = list(sets)[0]
    for i in range(1, len(sets)):
        cur = list(sets)[i]
        if cur == last + 1:
            last = cur
        else:
            appends(ans, start, last)
            start = last = cur

    appends(ans, start, last)
    print(",".join(ans))


if __name__ == '__main__':
    while 1:
        try:
            input_str = input().replace("\n", "")
            request = int(input())

            main(input_str, request)
        except Exception as e:
            break

    # 20-21,15,18,30,5-10
