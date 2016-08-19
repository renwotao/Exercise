#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	datetime 是 Python处理日期和时间的标准库
'''

# 获取当前日期和时间

# datetime 模块中 datetime 类
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

# 获取制定日期和时间

from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

# datetime 转换为 timestamp
'''
	在计算机中，时间实际上是用数字表示的。
	把1970年1月1日 00:00:00 UTC+00:00 时区的时刻称为 epoch time，
	记为 0 （1970年以前的时间 timestamp 为负数），
	当前时间就是相当于 epoch time 的秒数，称为 timestamp
'''

'''
	可以认为：
	timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
	对应的北京时间是：
	timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

	可见timestamp的值与时区毫无关系，因为timestamp一旦确定，
        其 UTC 时间就确定了，转换到任意时间也是完全确定的，
	这就是为什么计算机存储的当前时间是以 timestamp表示的，
	因为全球各地的计算机在任意时刻的timestamp都是完全相同的。
'''

from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20) # 用制定日期时间创建 datetime
print(dt.timestamp()) # 把datetime 转换为 timestamp

# 注意 Python 的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。


# timestamp 转换为 datetime
from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# 注意到 timestamp 是一个浮点数，它没有时区的概念，而datetime是有时区的。
# 上述转换是 timestamp 和本地时间做转换。
# 本地时间是指当前操作系统设定的时间。

'''
	例如北京时区是东8区，则本地时间：
	2015-04-19 12:20:00
	实际上就是UTC+8:00时区的时间：
	2015-04-19 12:20:00 UTC+8:00
	而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区应该是：
	2015-04-19 04:20:00 UTC+0:00
'''

# timestamp 也可以直接被转换到 UTC 标准时区的时间
from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

# str 转换为 datetime
from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)  # 注意转换后的 datetime 事没有时区信息的

# datetime 转换为 str
from datetime import datetime
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


# datetime 加减
'''
	对日期和时间进行加减实际上就是把 datetime 往后或往前计算，
	得到新的 datetime。
	加减可以直接用 + 和 - 运算符，不过需要导入 timedelta这个类
'''
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))


# 本地时间转换为 UTC 时间
'''
	本地时间是指系统设定时区的时间
	例如北京时间是 UTC+8:00时区的时间，而 UTC时间指 UTC+0:00时区的时间

	一个 datetime 类型有一个时区属性 tzinfo，但默认为 None，
	所以无法区分这个 datetime 到底是哪个时区，
	除非强型给 datetime设置一个时区
'''
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区 UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为 UTC+8:00
print(dt)

'''
	如果系统时区恰好是 UTC+8:00，那么上述代码就是正确的，
	否则，不能强制设置为UTC_8时区
'''

# 时区转换
# 可以通过 utcnow() 拿到当前的 UTC 时间，再转换为任意时区的时间

# 拿到 UTC 时间，并强制设置时区为 UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone() 将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone() 将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone() 将bj_dt 转换时区为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

'''
	时间转换的关键在于，拿到一个 datetime 时，要获知其正确的时区，
	然后强制设置时区，作为基准时间

	利用带时区的 datetime，通过 astimezone() 方法，可以转换到任意时区。

	注：不是必须从 UTC+0:00 时区转换到其他时区，
	    任何带时区的 datetime 都可以正确转换
'''

'''
	datetime 表示的时间需要时区信息才能确定一个特定的时间，
	否则只能视为本地时间。

	如果要存储 datetime，最佳方法是将其转换为 timestamp 再存储，
	因为 timestamp 的值与时区完全无关。
'''
