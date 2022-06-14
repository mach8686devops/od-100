# 身高体重排序

import sys

while 1:
    try:
        n = int(input())
        line = sys.stdin.readline().strip()
        heights = list(map(int, line.split()))

        line_two = sys.stdin.readline().strip()
        weights = list(map(int, line_two.split()))
        # print(heights, weights)

        ans = [(i + 1, m, n) for i, m, n in zip(list(range(n)), heights, weights)]


        class Student:
            def __init__(self, no, height, weight):
                self.no = no
                self.height = height
                self.weight = weight

            def __repr__(self):
                return repr((self.no, self.height, self.weight))

            def __str__(self):
                return repr((self.no, self.height, self.weight))


        students = [Student(x, y, z) for x, y, z in ans]

        from operator import attrgetter

        # ret = sorted(students, key=attrgetter('height', 'weight'))
        ret = sorted(ans, key=lambda x: (x[1], x[2]))
        # ans = [student.no for student in ret]
        ans = [x[0] for x in ret]
        print("".join([str(i) for i in ans]))

    except Exception as e:
        print(e)
        break

# 3
# 90 110 90
# 45 60 45
# 132
# 4
# 100 100 120 130
# 40 30 60 50
# 2134