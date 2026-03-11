import redis
import time

# 连接redis
redis_connect_pool = redis.ConnectionPool(
    host='free-test.redis.rds.aliyuncs.com',
    port=6379,
    password='jOub9uga3sun2miK',
    db=1
)

r = redis.Redis(connection_pool=redis_connect_pool)


# uid为需要更新账号生成时间的uid，x为需要提前推进的天数
# 会根据nut是否为0来判断该uid是游客还是登录用户
# nut   设备注册时间
# ar_t  账号注册时间
def change_x_days_to_hui(x, uid):
    hui_key = 'h:u:i:' + uid
    # hui_value = r.hgetall(hui_key)
    # print(hui_value)

    # ar_t为账号生成时间
    hui_ar_t = str(r.hget(hui_key, 'ar_t').decode('utf-8'))
    # 将获得到的ar_t转换为时间戳形式
    hui_ar_t_int = int(hui_ar_t)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    ar_t_time_local = time.localtime(hui_ar_t_int)
    # ar_t_time为年月日时分秒时间格式
    ar_t_time = time.strftime("%Y-%m-%d %H:%M:%S", ar_t_time_local)

    # nut为新账号注册时间
    hui_nut = str(r.hget(hui_key, 'nut').decode('utf-8'))
    # 将获得到的nut转换为时间戳形式
    hui_nut_int = int(hui_nut)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    nut_time_local = time.localtime(hui_nut_int)
    # nut_time为年月日时分秒时间格式
    nut_time = time.strftime("%Y-%m-%d %H:%M:%S", nut_time_local)

    print('uid为' + uid + '的用户')
    print('nut:' + hui_nut)
    print('nut时间戳对应的时间为' + nut_time)
    print('ar_t:' + hui_ar_t)
    print('ar_t时间戳对应的时间为' + ar_t_time)

    print('--------------------------------------------------------------')

    # x天的总秒数
    delta_seconds = x * 60 * 60 * 24

    # 如果nut值为0，说明该uid为游客uid
    if hui_nut == '0':
        print('该uid为游客')
        # 得到当前时间减去x天后的时间戳
        now_time = int(time.time())
        # 将游客账号的生成时间戳改为当前时间的天后
        new_hui_ar_t = now_time - delta_seconds

        flag_t = r.hset(hui_key, 'ar_t', new_hui_ar_t)
        # flag为0说明更新字段成功
        if flag_t == 0:
            print('更新游客' + uid + '的账号生成时间到' + str(x) + '天前成功')
            print('更新后的at_t时间戳为' + str(new_hui_ar_t))
            print('对应的时间为' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(new_hui_ar_t))))
        else:
            print(hui_key + '不存在')

    else:  # 说明nut不为0，即该账号为用户账号
        print('该uid为登录用户')
        # 得到当前时间减去x天后的时间戳
        now_time = int(time.time())
        # 将用户账号的生成时间戳改为当前时间的天后
        new_hui_nut = now_time - delta_seconds

        flag_u = r.hset(hui_key, 'nut', new_hui_nut)
        # flag为0说明更新字段成功
        if flag_u == 0:
            print('更新登录用户' + uid + '的账号注册时间到' + str(x) + '天前成功')
            print('更新后的nut时间戳为' + str(new_hui_nut))
            print('对应的时间为' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(new_hui_nut))))
        else:
            print(hui_key + '不存在')


# 将当前uid的账号注册时间设置为当前时间之前的x天
change_x_days_to_hui(9, '505128269')

