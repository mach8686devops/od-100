# TLV解码
while 1:
    try:
        Tag = input()

        dct = {}
        nums = input().split()

        key = None
        lens = None
        while nums:
            if key:
                if lens:
                    # 根据 整型信元长度 截取 Value
                    dct[key] = nums[0:int(lens)]
                    nums = nums[int(lens):]
                    key = None
                    lens = None
                else:
                    # 获取两字节信元长度
                    lens = int("".join(nums[0:2][::-1]))
                    nums = nums[2:]
            else:
                # 获取信元的Tag
                key = nums[0]
                nums = nums[1:]
            # 输出目标 信元 的 Value
            # dct = {'32': ['AE'], '90': ['01', '02'], '30': ['AB', '32', '31'], '31': ['32', '33'], '33': ['CC']}
        print(" ".join(dct[Tag]))
    except Exception as e:
        break
