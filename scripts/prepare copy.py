# import datetime, time

# now_time1 = time.strftime('%Y-%m-%dT%H:%M:%S')
# now_time2 = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
# print(now_time1)
# print(now_time2)


'''
import datetime

time1 = datetime.datetime(year=2018,month=12, day=21)
time2 = time1.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
print(time2)

'''

import datetime

timenow =( datetime.datetime.utcnow() + datetime.timedelta(days=10,hours=8)) #将utc时间转化为本地时间
a = datetime.datetime.utcnow()
b = datetime.datetime.utcnow().isoformat()
print(datetime.datetime.utcnow())
print(type(a))
print(type(b))

print((datetime.datetime.utcnow() + datetime.timedelta(hours=8)).isoformat() + "+08:00" ) #格式化字符串
c = a.timestamp()  # 日期转 时间戳
print(datetime.datetime.utcnow().timestamp())
print(type(c))
# print((datetime.datetime.utcnow() + datetime.timedelta(hours=8)).timestamp())
d = datetime.datetime.fromtimestamp(c)  # 时间戳转 日期
print(datetime.datetime.fromtimestamp(c))
print(type(d))

utc = "2018-07-17T08:48:31.151Z"
UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
utcTime = datetime.datetime.strptime(utc, UTC_FORMAT) #字符串转 datetime
localtime = utcTime + datetime.timedelta(hours=8)
x = localtime.timestamp()
y = datetime.datetime.fromtimestamp(x)
print(utcTime)
print(type(utcTime))
print(localtime)
print(x)
print(y)

