# 同班的小朋友

while 1:
    try:
        nums = input().split()

        # 第一个同学
        start = nums[0].split('/')
        A = [start[0]]
        B = []

        temp = [A, B]  # 表示前一个同学的班级， 默认是 A 班级
        # 从第二个同学开始判断
        for n in nums[1:]:
            id_, f = n.split("/")

            if f == "Y":
                temp = temp
            else:
                temp = temp[::-1]

            temp[0].append(id_)

        if A:
            print("".join(A))
        if B:
            print("".join(B))
    except Exception as e:
        break
