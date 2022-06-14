# 整数对最小和
while 1:
    try:
        array1 = list(map(int, input().split()))[1:]
        array2 = list(map(int, input().split()))[1:]
        k = int(input())

        dp = []
        for i in array1:
            for j in array2:
                dp.append(i+j)

        dp = sorted(dp)
        print(sum(dp[:2]))
    except Exception as e:
        break
