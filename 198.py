# words重量
while 1:
    try:
        nums = input().split()
        print(round(sum([len(i) for i in nums])/len(nums), 2))
    except Exception as e:
        break

