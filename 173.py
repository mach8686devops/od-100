# 解密犯罪时间
import datetime


while 1:
    try:
        time_ = input()
        pass_time = datetime.datetime.strptime(f"2020-05-31 {time_}", '%Y-%m-%d %H:%M')

        while 1:
            pass_time += datetime.timedelta(minutes=1)
            hm_ = pass_time.strftime('%H:%M')
            for c in hm_:
                if c not in time_:
                    break
            else:
                break
        print(hm_)
    except Exception as e:
        break
